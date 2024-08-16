import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Function to build LangGraph from a dataset
def build_langraph_from_dataset(file_path):
    df = pd.read_csv(file_path)
    G = nx.Graph()

    for _, row in df.iterrows():
        # Create a user node based on main category, sub category, and ratings
        user_node = f"User_{row['main_category']}_{row['sub_category']}_{row['ratings']}"
        G.add_node(user_node, main_category=row['main_category'], sub_category=row['sub_category'], ratings=row['ratings'])

        # Create a gift node based on the product's link
        gift_node = row['link']
        if not G.has_node(gift_node):
            G.add_node(gift_node, type="Gift", discount_price=row['discount_price'], actual_price=row['actual_price'], link=row['link'], image=row['image'])

        G.add_edge(user_node, gift_node, no_of_ratings=row['no_of_ratings'])

    return G

# Function to count gifts based on selected criteria
def count_gifts_by_criteria(G, main_category=None, sub_category=None, ratings=None, no_of_ratings=None):
    gift_counts = {}
    for node, data in G.nodes(data=True):
        if (main_category is None or data.get('main_category') == main_category) and \
           (sub_category is None or data.get('sub_category') == sub_category) and \
           (ratings is None or data.get('ratings') == ratings):
            for neighbor in G.neighbors(node):
                if G.nodes[neighbor].get('type') == 'Gift' and \
                   (no_of_ratings is None or G.edges[node, neighbor].get('no_of_ratings') == no_of_ratings):
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
    csv_file_path = 'amazon.csv'  # Path to your dataset
    G = build_langraph_from_dataset(csv_file_path)

    st.write("Choose criteria to analyze gift counts:")

    main_category = st.selectbox("Select Main Category", options=[None] + sorted({str(G.nodes[node]['main_category']) for node in G.nodes if 'main_category' in G.nodes[node]}))
    sub_category = st.selectbox("Select Sub Category", options=[None] + sorted({str(G.nodes[node]['sub_category']) for node in G.nodes if 'sub_category' in G.nodes[node]}))
    ratings = st.selectbox("Select Ratings", options=[None] + sorted({str(G.nodes[node]['ratings']) for node in G.nodes if 'ratings' in G.nodes[node]}))
    no_of_ratings = st.selectbox("Select Number of Ratings", options=[None] + sorted({str(G.edges[edge]['no_of_ratings']) for edge in G.edges if 'no_of_ratings' in G.edges[edge]}))

    if st.button("Analyze"):
        gift_counts = count_gifts_by_criteria(G, main_category, sub_category, ratings, no_of_ratings)
        title = "Number of Gifts"
        if main_category:
            title += f" for {main_category}"
        if sub_category:
            title += f" in Sub Category {sub_category}"
        if ratings:
            title += f" with Ratings {ratings}"
        if no_of_ratings:
            title += f" and Number of Ratings {no_of_ratings}"

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
