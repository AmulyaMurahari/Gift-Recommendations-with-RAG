import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Function to build LangGraph from a dataset
def build_langraph_from_dataset(file_path):
    df = pd.read_csv(file_path)
    G = nx.Graph()

    for _, row in df.iterrows():
        user_node = f"User_{row['Age']}_{row['Gender']}_{row['Relationship']}_{row['Interest']}"
        G.add_node(user_node, age=row['Age'], gender=row['Gender'], relationship=row['Relationship'], interest=row['Interest'])

        gift_node = row['Gift']
        if not G.has_node(gift_node):
            G.add_node(gift_node, type="Gift", rating=row['Rating'], price_range=f"${row['Budget']}-$${row['MaxBudget']}", link=row['Link'])

        G.add_edge(user_node, gift_node, occasion=row['Occasion'])

    return G

# Function to count gifts based on selected criteria
def count_gifts_by_criteria(G, gender=None, age=None, relationship=None, interest=None, occasion=None):
    gift_counts = {}
    for node, data in G.nodes(data=True):
        if (gender is None or data.get('gender') == gender) and \
           (age is None or data.get('age') == age) and \
           (relationship is None or data.get('relationship') == relationship) and \
           (interest is None or data.get('interest') == interest):
            for neighbor in G.neighbors(node):
                if G.nodes[neighbor].get('type') == 'Gift' and \
                   (occasion is None or G.edges[node, neighbor].get('occasion') == occasion):
                    gift_counts[neighbor] = gift_counts.get(neighbor, 0) + 1
    return gift_counts

# Function to visualize the count of gifts based on criteria
def visualize_gifts_by_criteria(gift_counts, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(gift_counts.keys(), gift_counts.values(), color='skyblue')
    ax.set_title(title)
    ax.set_xlabel("Gifts")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="LangGraph Analysis")
    st.header("LangGraph Gift Analysis")

    # Load the dataset and build the LangGraph
    csv_file_path = 'dataset.csv'  # Path to your dataset
    G = build_langraph_from_dataset(csv_file_path)

    st.write("Choose criteria to analyze gift counts:")

    gender = st.selectbox("Select Gender", options=[None, "Male", "Female"])
    age = st.selectbox("Select Age", options=[None] + sorted({G.nodes[node]['age'] for node in G.nodes if 'age' in G.nodes[node]}))
    relationship = st.selectbox("Select Relationship", options=[None] + sorted({G.nodes[node]['relationship'] for node in G.nodes if 'relationship' in G.nodes[node]}))
    interest = st.selectbox("Select Interest", options=[None] + sorted({G.nodes[node]['interest'] for node in G.nodes if 'interest' in G.nodes[node]}))
    occasion = st.selectbox("Select Occasion", options=[None] + sorted({G.edges[edge]['occasion'] for edge in G.edges if 'occasion' in G.edges[edge]}))

    if st.button("Analyze"):
        gift_counts = count_gifts_by_criteria(G, gender, age, relationship, interest, occasion)
        title = "Number of Gifts"
        if gender:
            title += f" for {gender}"
        if age:
            title += f" of Age {age}"
        if relationship:
            title += f" for {relationship}"
        if interest:
            title += f" interested in {interest}"
        if occasion:
            title += f" for {occasion}"

        if gift_counts:
            visualize_gifts_by_criteria(gift_counts, title)
        else:
            st.write("No matching gifts found.")

    with st.sidebar:
        st.title("Menu:")
        if st.button("Show LangGraph Visualization"):
            st.subheader("LangGraph Visualization")
            # Draw the graph
            fig, ax = plt.subplots(figsize=(15, 15))
            pos = nx.spring_layout(G, k=0.3)
            nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.5)
            nx.draw_networkx_nodes(G, pos, ax=ax, node_size=700, node_color='skyblue')
            nx.draw_networkx_labels(G, pos, ax=ax, font_size=8, font_weight='bold')
            st.pyplot(fig)

if __name__ == "__main__":
    main()
