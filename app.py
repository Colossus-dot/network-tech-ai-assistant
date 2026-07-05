import streamlit as st

st.set_page_config(
    page_title="Network Tech AI Assistant",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Network Tech AI Assistant")
st.write("Troubleshoot common network problems fast.")

issue = st.selectbox(
    "What problem are you troubleshooting?",
    [
        "No Internet Connection",
        "DNS Problem",
        "DHCP Problem",
        "Slow Network",
        "Cannot Reach Default Gateway",
        "Server Offline"
    ]
)

if st.button("Get Troubleshooting Steps"):
    if issue == "No Internet Connection":
        st.write("1. Check physical cable or Wi-Fi connection.")
        st.write("2. Verify the device has a valid IP address.")
        st.write("3. Ping the default gateway.")
        st.write("4. Ping 8.8.8.8.")
        st.write("5. Test DNS resolution.")

    elif issue == "DNS Problem":
        st.write("1. Ping an IP address such as 8.8.8.8.")
        st.write("2. Run nslookup on the domain.")
        st.write("3. Verify DNS server settings.")
        st.write("4. Clear the DNS cache.")

    elif issue == "DHCP Problem":
        st.write("1. Check for a 169.254.x.x address.")
        st.write("2. Renew the DHCP lease.")
        st.write("3. Verify the DHCP server is running.")
        st.write("4. Check VLAN and relay settings.")

    elif issue == "Slow Network":
        st.write("1. Check latency and packet loss.")
        st.write("2. Test wired versus wireless.")
        st.write("3. Check interface utilization.")
        st.write("4. Look for duplex or speed mismatches.")

    elif issue == "Cannot Reach Default Gateway":
        st.write("1. Verify IP address and subnet mask.")
        st.write("2. Confirm the default gateway address.")
        st.write("3. Check VLAN assignment.")
        st.write("4. Inspect switch port status.")

    elif issue == "Server Offline":
        st.write("1. Check power and link lights.")
        st.write("2. Ping the server IP.")
        st.write("3. Check switch port status.")
        st.write("4. Verify routing and firewall rules.")
