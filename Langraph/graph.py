import pandas as pd  # Import pandas for data handling
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

# Function to build a normal graph from a dataset
def build_normal_graph(file_path):
    df = pd.read_csv(file_path)
    G = nx.Graph()

    # Add edges between users and gifts (basic connections)
    for _, row in df.iterrows():
        user_node = f"User_{row['Age']}_{row['Gender']}_{row['Relationship']}"
        gift_node = row['Gift']

        if not G.has_node(user_node):
            G.add_node(user_node)

        if not G.has_node(gift_node):
            G.add_node(gift_node)

        G.add_edge(user_node, gift_node)  # Simple edge without contextual information

    return G

# Function to filter the graph based on selected criteria
def filter_graph(G, gender=None, age=None, relationship=None, gift=None):
    subgraph_nodes = []
    
    for node, data in G.nodes(data=True):
        if gender and gender not in node:
            continue
        if age and f"_{age}_" not in node:
            continue
        if relationship and relationship not in node:
            continue
        if gift and node != gift and not G.has_edge(node, gift):
            continue
        
        subgraph_nodes.append(node)
    
    return G.subgraph(subgraph_nodes)

# Function to visualize the normal graph
def visualize_normal_graph(G, title="Normal Graph Visualization"):
    fig, ax = plt.subplots(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold', edge_color='gray', ax=ax)
    plt.title(title)
    st.pyplot(fig)

# Main function to run the Streamlit app for normal graph
def main():
    st.set_page_config(page_title="Normal Graph Analysis")
    st.header("Normal Graph Gift Analysis")

    # Load the dataset and build the normal graph
    csv_file_path = 'dataset.csv'  # Path to your dataset
    G = build_normal_graph(csv_file_path)

    # Dropdowns for filtering
    st.write("Filter the graph based on the criteria below:")

    gender = st.selectbox("Select Gender", options=[None, "Male", "Female"])
    age = st.selectbox("Select Age", options=[None] + sorted({G.nodes[node].split('_')[1] for node in G.nodes if node.startswith("User")}))
    relationship = st.selectbox("Select Relationship", options=[None] + sorted({G.nodes[node].split('_')[2] for node in G.nodes if node.startswith("User")}))
    gift = st.selectbox("Select Gift", options=[None] + sorted({node for node in G.nodes if not node.startswith("User")}))

    if st.button("Show Filtered Graph"):
        filtered_G = filter_graph(G, gender=gender, age=age, relationship=relationship, gift=gift)
        visualize_normal_graph(filtered_G, title="Filtered Normal Graph Visualization")

    with st.sidebar:
        st.title("Menu:")
        if st.button("Show Full Normal Graph Visualization"):
            st.subheader("Full Normal Graph Visualization")
            visualize_normal_graph(G, title="Full Normal Graph Visualization")

if __name__ == "__main__":
    main()
