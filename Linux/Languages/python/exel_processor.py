# streamlit run exel_processor.py
import streamlit as st
import pandas as pd
import io
import os
 
st.set_page_config(page_title="Excel Data Reviewer", page_icon="📊", layout="wide")
 
st.title("📊 Excel Data Reviewer")
st.markdown("Upload large Excel or CSV files to quickly preview, filter, and analyze the data.")
 
# Initialize session state for the dataframes
if 'dfs' not in st.session_state:
    st.session_state.dfs = {}
 
# Constants for safety limit
MAX_FILE_SIZE_MB = 1000
 
# SECURITY: Set to False before deploying to a public server!
# If True, anyone using the app can attempt to read ANY csv/excel file on the server's hard drive.
ALLOW_LOCAL_FILE_READ = False
 
# Sidebar for file upload
with st.sidebar:
    st.header("Import Data")
    
    if ALLOW_LOCAL_FILE_READ:
        import_method = st.radio("Choose Import Method:", ["Upload via Browser", "Direct Local Path (Best for >500MB)"])
    else:
        import_method = "Upload via Browser"
        st.info("Direct Local Path import is disabled for security.")
    
    if import_method == "Upload via Browser":
        uploaded_files = st.file_uploader("Choose files", type=["xlsx", "csv"], accept_multiple_files=True)
        st.caption("🚀 Powered by High-Performance Engines (PyArrow & Calamine)")
        st.caption(f"🛡️ Max supported file size: {MAX_FILE_SIZE_MB}MB")
        
        if uploaded_files:
            with st.spinner("Loading data at high speed... (Browser might freeze momentarily for massive files)"):
                for uploaded_file in uploaded_files:
                    if uploaded_file.name not in st.session_state.dfs:
                        # Safety check: enforce file size limit
                        file_size_mb = uploaded_file.size / (1024 * 1024)
                        if file_size_mb > MAX_FILE_SIZE_MB:
                            st.error(f"File {uploaded_file.name} is too large ({file_size_mb:.1f}MB). Max limit is {MAX_FILE_SIZE_MB}MB.")
                            continue
                            
                        try:
                            if uploaded_file.name.endswith('.csv'):
                                df = pd.read_csv(uploaded_file, engine='pyarrow')
                            else:
                                df = pd.read_excel(uploaded_file, engine='calamine')
                            st.session_state.dfs[uploaded_file.name] = df
                        except Exception as e:
                            st.error(f"Error loading {uploaded_file.name}. Details: {e}")
                if uploaded_files:
                    st.success("Files loaded successfully!")
                    
    elif ALLOW_LOCAL_FILE_READ:
        st.info("💡 Bypasses the browser limits entirely. Much faster for massive files.")
        local_path = st.text_input("Enter the absolute file path:", placeholder="/home/eld0c/Documentos/huge_data.xlsx")
        
        if st.button("Load Local File"):
            if local_path and os.path.exists(local_path):
                filename = os.path.basename(local_path)
                if filename not in st.session_state.dfs:
                    with st.spinner(f"Reading {filename} directly from disk..."):
                        try:
                            if filename.endswith('.csv'):
                                df = pd.read_csv(local_path, engine='pyarrow')
                            else:
                                df = pd.read_excel(local_path, engine='calamine')
                            st.session_state.dfs[filename] = df
                            st.success(f"{filename} loaded successfully!")
                        except Exception as e:
                            st.error(f"Error loading {filename}. Details: {e}")
            elif local_path:
                st.error("File not found! Please check the path and try again. E.g /home/eld0c/Documentos/file.xlsx")
 
# Main content area
if st.session_state.dfs:
    # Select which file to view
    selected_file = st.selectbox("Select file to analyze:", list(st.session_state.dfs.keys()))
    df = st.session_state.dfs[selected_file]
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / (1024 * 1024):.2f} MB")
    
    st.divider()
    
    # Filtering controls
    st.subheader("Filter Data")
    
    # Global search
    search_term = st.text_input("Global Search (All Columns):", help="Search for a term across all columns")
    filtered_df = df.copy()
    
    if search_term:
        mask = filtered_df.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)
        filtered_df = filtered_df[mask]
        
    # Multi-column specific filtering
    st.markdown("### Specific Column Filters (AND condition)")
    filter_cols = st.multiselect("Select columns to add specific filters:", list(df.columns))
    
    if filter_cols:
        cols = st.columns(min(len(filter_cols), 3))
        for i, col in enumerate(filter_cols):
            with cols[i % 3]:
                col_type = df[col].dtype
                if pd.api.types.is_numeric_dtype(col_type):
                    # Numeric filter
                    min_val = float(df[col].min()) if not pd.isna(df[col].min()) else 0.0
                    max_val = float(df[col].max()) if not pd.isna(df[col].max()) else 100.0
                    if min_val == max_val:
                        st.info(f"{col}: All values are {min_val}")
                    else:
                        filter_val = st.slider(f"Range for {col}:", min_value=min_val, max_value=max_val, value=(min_val, max_val), key=f"filter_{col}")
                        filtered_df = filtered_df[(filtered_df[col] >= filter_val[0]) & (filtered_df[col] <= filter_val[1])]
                else:
                    # Categorical / Text filter
                    unique_vals = df[col].dropna().unique()
                    if len(unique_vals) < 50:
                        filter_val = st.multiselect(f"Select {col} values:", options=list(unique_vals), key=f"filter_{col}")
                        if filter_val:
                            filtered_df = filtered_df[filtered_df[col].isin(filter_val)]
                    else:
                        filter_val = st.text_input(f"Text in {col} contains:", key=f"filter_{col}")
                        if filter_val:
                            filtered_df = filtered_df[filtered_df[col].astype(str).str.contains(filter_val, case=False, na=False)]
                            
    st.write(f"**Found {filtered_df.shape[0]} matching rows.**")
    
    # Display the dataframe with pagination (Streamlit's dataframe handles large datasets reasonably well with scrolling, but we can limit rows for performance)
    st.subheader("Data Preview")
    
    # Column selection
    all_columns = filtered_df.columns.tolist()
    selected_columns = st.multiselect("Select columns to view:", options=all_columns, default=all_columns)
    
    # Options for viewing
    view_option = st.radio("Rows to display:", ["First 1000", "First 5000", "All (may be slow)"], horizontal=True)
    
    display_df = filtered_df[selected_columns]
    
    if view_option == "First 1000":
        display_df = display_df.head(1000)
    elif view_option == "First 5000":
        display_df = display_df.head(5000)
        
    st.dataframe(display_df, use_container_width=True)
    
    # Export filtered data
    csv = filtered_df[selected_columns].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Gathered Data as CSV",
        data=csv,
        file_name='gathered_data.csv',
        mime='text/csv',
    )
    
    st.divider()
    
    # Basic Data Gathering & Grouping
    st.subheader("Gather Data Summaries")
    st.markdown("Group your data by a specific column to gather insights (e.g. Total sales by category).")
    
    col_group, col_agg, col_target = st.columns(3)
    with col_group:
        group_by_col = st.selectbox("Group By:", ["None"] + all_columns)
    with col_target:
        target_cols = [c for c in all_columns if pd.api.types.is_numeric_dtype(df[c])]
        if target_cols:
            agg_col = st.selectbox("Column to Aggregate:", ["None"] + target_cols)
        else:
            agg_col = "None"
            st.info("No numeric columns found for aggregation.")
    with col_agg:
        agg_func = st.selectbox("Function:", ["Sum", "Average", "Count", "Minimum", "Maximum"])
    
    if group_by_col != "None" and agg_col != "None":
        func_map = {"Sum": "sum", "Average": "mean", "Count": "count", "Minimum": "min", "Maximum": "max"}
        try:
            summary_df = filtered_df.groupby(group_by_col)[agg_col].agg(func_map[agg_func]).reset_index()
            st.dataframe(summary_df, use_container_width=True)
        except Exception as e:
            st.error(f"Could not calculate summary: {e}")
    elif group_by_col != "None" and agg_col == "None" and agg_func == "Count":
        # If they just want to count occurrences in a group without a target metric
        summary_df = filtered_df[group_by_col].value_counts().reset_index()
        summary_df.columns = [group_by_col, 'Count']
        st.dataframe(summary_df, use_container_width=True)
    
    # Column details
    with st.expander("Show Column Data Types"):
        dtypes_df = pd.DataFrame(df.dtypes, columns=['Data Type']).reset_index()
        dtypes_df.rename(columns={'index': 'Column Name'}, inplace=True)
        dtypes_df['Data Type'] = dtypes_df['Data Type'].astype(str)
        st.dataframe(dtypes_df, hide_index=True)
 
else:
    st.info("👈 Please upload a file from the sidebar to begin.")