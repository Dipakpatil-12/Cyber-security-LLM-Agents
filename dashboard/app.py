import streamlit as st
import pandas as pd
from ai_analyzer import analyze_security_logs

st.set_page_config(
    page_title="AI CyberShield",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: white;
}
[data-testid="stMetric"] {
    background: #172338;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #26364f;
}
h1, h2, h3, p {
    color: #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ AI CyberShield")
st.caption("Cybersecurity Threat Detection & Analytics Dashboard")
st.success("● Dashboard Online — Demo Mode")

# Security Overview
st.markdown("## Security Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Security Events", "12,845", "+12%")
c2.metric("Threats Detected", "27", "+5")
c3.metric("Critical Alerts", "3", "Needs review")
c4.metric("System Health", "98.4%", "Healthy")

st.caption("Demo metrics only — not connected to live security systems.")

st.divider()

# Security Charts
left, right = st.columns([2, 1])

with left:
    st.subheader("📈 Security Events")

    chart_data = pd.DataFrame({
        "Normal Events": [120, 150, 130, 180, 160, 210, 190],
        "Suspicious Events": [5, 8, 4, 12, 7, 15, 10]
    }, index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

    st.line_chart(chart_data)

with right:
    st.subheader("🚨 Threat Severity")
    st.write("🔴 Critical: 3")
    st.progress(0.15)
    st.write("🟠 High: 8")
    st.progress(0.40)
    st.write("🟡 Medium: 16")
    st.progress(0.80)

st.divider()

# Recent Security Events
st.subheader("📋 Recent Security Events")

data = pd.DataFrame([
    ["20:41", "192.168.1.24", "Repeated failed logins", "HIGH", "Investigate"],
    ["20:38", "10.0.0.18", "Successful login", "LOW", "Normal"],
    ["20:32", "185.22.11.7", "Unusual access pattern", "CRITICAL", "Review"],
    ["20:25", "192.168.1.50", "Multiple login attempts", "MEDIUM", "Monitor"],
    ["20:19", "10.0.0.21", "Successful login", "LOW", "Normal"]
], columns=["Time", "Source IP", "Event", "Severity", "Status"])

severity = st.selectbox(
    "Filter by severity",
    ["ALL", "CRITICAL", "HIGH", "MEDIUM", "LOW"]
)

filtered_data = data.copy()

if severity != "ALL":
    filtered_data = filtered_data[
        filtered_data["Severity"] == severity
    ]

st.dataframe(
    filtered_data,
    use_container_width=True,
    hide_index=True
)

st.divider()

# Login Activity Rule
st.subheader("🔍 Analyze Login Activity")

attempts = st.number_input(
    "Enter failed login attempts",
    min_value=0,
    max_value=1000,
    value=0
)

if st.button("Analyze Activity"):
    if attempts >= 5:
        st.error("⚠️ Suspicious activity detected!")
        st.write(
            "Recommendation: Investigate the account "
            "and review its login history."
        )
    else:
        st.success(
            "No suspicious activity detected by this demo rule."
        )

st.divider()

# Security Log Analyzer
st.header("🛡️ Security Log Analyzer")

st.write(
    "Upload a security log file to analyze suspicious activities."
)

uploaded_file = st.file_uploader(
    "Upload Security Log File",
    type=["txt", "log", "csv"],
    key="security_log_upload"
)

if uploaded_file is not None:
    try:
        log_content = uploaded_file.getvalue().decode(
            "utf-8", errors="replace"
        )

        lines = log_content.splitlines()

        st.subheader("📄 Log Preview")
        st.text_area(
            "Uploaded Log Content",
            log_content,
            height=200
        )

        # Rule-based Detection
        failed_logins = [
            line for line in lines
            if "failed" in line.lower()
            or "failure" in line.lower()
        ]

        suspicious_events = [
            line for line in lines
            if any(
                word in line.lower()
                for word in [
                    "unauthorized",
                    "suspicious",
                    "attack"
                ]
            )
        ]

        st.subheader("📊 Security Analysis Results")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Log Entries", len(lines))
        col2.metric("Failed Login Matches", len(failed_logins))
        col3.metric(
            "Suspicious Keyword Matches",
            len(suspicious_events)
        )

        if failed_logins or suspicious_events:
            st.warning(
                "Potentially suspicious log entries found. "
                "Review the evidence before taking action."
            )

            if failed_logins:
                with st.expander("View Failed Login Events"):
                    for event in failed_logins[:50]:
                        st.text(event)

            if suspicious_events:
                with st.expander("View Suspicious Events"):
                    for event in suspicious_events[:50]:
                        st.text(event)
        else:
            st.success(
                "No matches for the configured security keywords."
            )

        # AI Log Analysis
        st.divider()
        st.subheader("🤖 AI Security Analysis")

        if st.button("Analyze Logs with AI"):
            with st.spinner("AI is analyzing the logs..."):
                result = analyze_security_logs(log_content)

            st.write(result)

        # AI Threat Detection
        if st.button("🛡️ Detect Security Threats"):
            threat_prompt = (
                "Analyze these security logs. Identify possible "
                "suspicious IPs, repeated failed logins, unauthorized "
                "access attempts, and potential security threats. "
                "For each finding, explain the evidence, possible "
                "severity, and recommended defensive actions. "
                "Do not claim a confirmed attack without sufficient "
                "evidence.\n\n"
                + log_content[:12000]
            )

            with st.spinner("Checking for potential threats..."):
                result = analyze_security_logs(threat_prompt)

            st.subheader("🚨 Threat Detection Report")
            st.write(result)

        # Download Report
        report = [
            "AI CyberShield - Security Analysis Report",
            "=" * 45,
            f"Total log entries: {len(lines)}",
            f"Failed login matches: {len(failed_logins)}",
            f"Suspicious keyword matches: {len(suspicious_events)}",
            "",
            "Failed Login Events:",
            *failed_logins[:50],
            "",
            "Suspicious Events:",
            *suspicious_events[:50],
            "",
            "Note: Keyword matches do not confirm a cyberattack."
        ]

        st.download_button(
            label="📥 Download Security Report",
            data="\n".join(report),
            file_name="cybershield_report.txt",
            mime="text/plain"
        )

        st.caption(
            "This dashboard analyzes uploaded logs using keyword "
            "matching and optional AI analysis. It does not provide "
            "continuous live monitoring."
        )

    except Exception as error:
        st.error(f"Unable to analyze the file: {error}")

else:
    st.info("Upload a .txt, .log, or .csv file to get started.")