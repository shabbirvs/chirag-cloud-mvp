import streamlit as st
import time
from agents.perception import run_perception
from agents.strategy import run_strategy
from agents.execution import format_output

st.set_page_config(page_title="CHIRAG Appliance OS", layout="wide")

# Header simulating on-premise hardware
st.title("🛡️ CHIRAG: Sovereign Digital Worker Appliance")
st.caption("Deployment Mode: Zero-Trust Local Node | Multi-Agent Architecture")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Ingestion Layer")
    preset = st.selectbox("Select Preset Demo:", ["Retail: New Apparel Batch", "Healthcare: RCM Encounter"])
    uploaded_file = st.file_uploader("Upload raw file or use preset", type=["jpg", "png", "pdf"])
    
    start_btn = st.button("Trigger Appliance Pipeline", type="primary")

if start_btn:
    with col2:
        st.subheader("2. Multi-Agent Processing")
        
        status_perception = st.status("Perception Agent: Processing visual features...", expanded=True)
        raw_features = run_perception(preset, uploaded_file)
        status_perception.update(label="Perception Agent: Completed", state="complete")
        
        status_strategy = st.status("Strategy Agent: Evaluating context & rules...", expanded=True)
        reasoned_plan = run_strategy(raw_features, preset)
        status_strategy.update(label="Strategy Agent: Strategy locked", state="complete")
        
        payload = format_output(reasoned_plan, preset)
        
        st.subheader("3. Sovereign Control Boundary")
        st.info("System paused. Awaiting human administrator authorization.")
        st.json(payload)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Approve & Dispatch"):
                st.success("Dispatched to local endpoint. Zero cloud data leakage.")
        with c2:
            if st.button("✏️ Modify / Override"):
                st.warning("Action halted by administrator.")