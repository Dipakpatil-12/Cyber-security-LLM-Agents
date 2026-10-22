import streamlit as st
import pandas as pd

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

st.markdown("## Security Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Security Events", "12,845", "+12%")
c2.metric("Threats Detected", "27", "+5")
c3.metric("Critical Alerts", "3", "Needs review")
c4.metric("System Health", "98.4%", "Healthy")

st.divider()

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

if severity != "ALL":
    data = data[data["Severity"] == severity]

st.dataframe(data, use_container_width=True, hide_index=True)

st.divider()

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
        st.write("Recommendation: Investigate the account and review its login history.")
    else:
        st.success("No suspicious activity detected by this demo rule.")

st.caption("Educational demo using sample data. Not connected to live security systems.")

st.divider()
st.header("📂 Upload Security Logs")

uploaded_file = st.file_uploader(
    "Upload a security log file",
    type=["txt", "log", "csv"]
)

if uploaded_file is not None:
    content = uploaded_file.getvalue().decode("utf-8", errors="replace")

    st.subheader("Log Preview")
    st.text_area("Uploaded Log Content", content, height=200)

    if st.button("Analyze Security Logs"):
        lines = content.splitlines()

        failed = sum(
            1 for line in lines
            if "failed" in line.lower() or "failure" in line.lower()
        )

        suspicious = sum(
            1 for line in lines
            if "suspicious" in line.lower()
            or "unauthorized" in line.lower()
        )

        st.metric("Failed Login Events", failed)
        st.metric("Suspicious Log Entries", suspicious)

        if failed >= 5 or suspicious > 0:
            st.warning(
                "Potentially suspicious activity found. "
                "Review the original logs before taking action."
            )
        else:
            st.success("No matching suspicious patterns found.")
