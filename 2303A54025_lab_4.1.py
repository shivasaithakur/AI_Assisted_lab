# Intent Classification using Zero-shot, One-shot, and Few-shot Prompting (Simulation)

INTENTS = ["Account Issue", "Order Status", "Product Inquiry", "General Question"]

# ---------------------------
# ZERO-SHOT CLASSIFICATION
# ---------------------------
def zero_shot_intent(query):
    q = query.lower()

    if any(word in q for word in ["login", "log in", "password", "reset", "account"]):
        return "Account Issue"
    elif any(word in q for word in ["order", "shipping", "track", "delayed"]):
        return "Order Status"
    elif any(word in q for word in ["phone", "laptop", "sell", "price", "deals", "hdmi"]):
        return "Product Inquiry"
    else:
        return "General Question"


# ---------------------------
# ONE-SHOT CLASSIFICATION
# ---------------------------
def one_shot_intent(query):
    q = query.lower()

    # Slight bias toward account problems because of one example
    if any(word in q for word in ["login", "password", "reset", "account", "link"]):
        return "Account Issue"
    elif any(word in q for word in ["order", "shipping", "track"]):
        return "Order Status"
    elif any(word in q for word in ["phone", "laptop", "deals", "hdmi"]):
        return "Product Inquiry"
    else:
        return "General Question"


# ---------------------------
# FEW-SHOT CLASSIFICATION
# ---------------------------
def few_shot_intent(query):
    q = query.lower()

    # Overfitting mistake due to multiple examples related to account issues
    if any(word in q for word in ["login", "password", "reset", "account", "return", "policy"]):
        return "Account Issue"   # Incorrect bias
    elif any(word in q for word in ["order", "shipping"]):
        return "Order Status"
    elif any(word in q for word in ["phone", "laptop", "deals", "hdmi"]):
        return "Product Inquiry"
    else:
        return "General Question"


# ---------------------------
# TEST QUERIES
# ---------------------------
test_queries = [
    "My password reset link expired",
    "Shipping delayed again",
    "Any Black Friday deals?",
    "What is your return policy?"
]

print("INTENT CLASSIFICATION RESULTS")
print("=" * 45)

for query in test_queries:
    print(f"\nQuery: {query}")
    print("Zero-shot :", zero_shot_intent(query))
    print("One-shot  :", one_shot_intent(query))
    print("Few-shot  :", few_shot_intent(query))
    print("-" * 45)

print("\nKey Insight: Few-shot prompting can sometimes become biased and misclassify queries like 'return policy' as an Account Issue.")
