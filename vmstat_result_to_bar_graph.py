import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Streamlit 설정
st.title("Dynamic Dataset Visualization Tool")

# 세션 상태 초기화
if "dataset_count" not in st.session_state:
    st.session_state.dataset_count = 1  # 초기 데이터셋 수
if "datasets" not in st.session_state:
    st.session_state.datasets = {}

# 데이터셋 추가 버튼
st.header("Input Datasets")
if st.button("Add Dataset"):
    st.session_state.dataset_count += 1

# 동적 데이터셋 입력
for i in range(1, st.session_state.dataset_count + 1):
    dataset_name = st.text_input(f"Dataset {i} Name", value=f"Dataset {i}", key=f"dataset_name_{i}")
    dataset_data = st.text_area(
        f"Paste data for {dataset_name}",
        placeholder="Metric Name Value1 Value2 Average\nExample: Free Memory (KB) 158500 4896392 341468.72",
        height=200,
        key=f"dataset_data_{i}",
    )
    if dataset_name and dataset_data.strip():
        st.session_state.datasets[dataset_name] = dataset_data.strip()

# 데이터셋 처리
if st.session_state.datasets:
    processed_data = []
    for dataset_name, data in st.session_state.datasets.items():
        lines = data.strip().split("\n")
        for line in lines:
            parts = line.split()
            metric_name = " ".join(parts[:-3])
            average_value = float(parts[-1])
            processed_data.append((dataset_name, metric_name, average_value))

    # DataFrame 생성
    df = pd.DataFrame(processed_data, columns=["Dataset", "Metric", "Average"])

    # 그룹화 규칙 정의
    groups = {
        "Memory": ["Free Memory (KB)", "Cache Memory (KB)"],
        "Blocks": ["Blocks In (blocks/s)", "Blocks Out (blocks/s)"],
        "Context Switches": ["Context Switches"],
        "CPU": ["User CPU (%)", "System CPU (%)", "Idle CPU (%)", "IO Wait (%)"],
    }

    # 그래프 시각화
    st.header("Visualization")
    for group_name, metrics in groups.items():
        group_df = df[df["Metric"].isin(metrics)]
        datasets = group_df["Dataset"].unique()
        x = np.arange(len(metrics))  # X 좌표 기본 위치
        bar_width = 0.2  # 막대 너비

        # Streamlit에 그래프 추가
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, dataset_name in enumerate(datasets):
            subset = group_df[group_df["Dataset"] == dataset_name]
            ax.bar(x + i * bar_width, subset["Average"], bar_width, label=dataset_name)

        ax.set_xticks(x + (len(datasets) - 1) * bar_width / 2)
        ax.set_xticklabels(metrics, rotation=45, ha="right")
        ax.set_title(f"{group_name} Averages")
        ax.set_ylabel("Average")
        ax.legend(title="Dataset")
        st.pyplot(fig)
