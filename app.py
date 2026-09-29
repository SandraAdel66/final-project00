"""
Fawry Home — Gradio implementation.

The screen is built entirely out of small, reusable component
functions defined in components.py. Swap the data below to reuse
the same layout for a different user / different transactions,
or reorder the `page([...])` call to reuse the same building
blocks in a new layout.

Run:
    python app.py
"""

import gradio as gr
import components as c

with open("style.css", "r", encoding="utf-8") as f:
    CUSTOM_CSS = f.read()


# ---------------------------------------------------------------------------
# Data — swap this out per-user; every function below is reusable/stateless
# ---------------------------------------------------------------------------

QUICK_PAY_ITEMS = [
    {"icon": "bolt", "label": "Electricity", "highlight": True},
    {"icon": "water", "label": "Water"},
    {"icon": "wifi", "label": "Internet"},
    {"icon": "mobile", "label": "Top-up"},
]

FEATURE_CARDS = [
    {
        "icon": "calendar",
        "title": "Taqseet",
        "subtitle": "Installments up to 24 months",
        "tag": "0% APR",
        "tag_color": "yellow",
    },
    {
        "icon": "chart",
        "title": "Investments",
        "subtitle": "Gold & funds from EGP 100",
        "tag": "From EGP 100",
        "tag_color": "yellow",
    },
    {
        "icon": "grid",
        "title": "Services",
        "subtitle": "Bills, tickets, donations",
        "tag": "300+ services",
        "tag_color": "yellow",
    },
    {
        "icon": "heart",
        "title": "For you",
        "subtitle": "Picks based on your spend",
        "tag": "Personalized",
        "tag_color": "purple",
    },
]

RECENT_PAYMENTS = [
    {"icon": "bolt", "name": "North Cairo Electricity", "meta": "Today • 10:24 AM", "amount": "- EGP 342.00"},
    {"icon": "mobile", "name": "Vodafone recharge", "meta": "Yesterday", "amount": "- EGP 100.00"},
    {"icon": "water", "name": "Cairo Water Company", "meta": "12 Sep", "amount": "- EGP 88.50"},
]

NAV_ITEMS = [
    {"key": "home", "icon": "home", "label": "Home"},
    {"key": "wallet", "icon": "wallet", "label": "Wallet"},
    {"key": "offers", "icon": "offers", "label": "Offers"},
    {"key": "pay", "icon": "pay", "label": "Quick pay"},
    {"key": "more", "icon": "more", "label": "More"},
]


def build_home_html() -> str:
    """Compose the page purely from reusable components."""
    sections = [
        c.header(user_name="Ahmed Mohamed", location="Cairo, Egypt", avatar_initial="A"),
        c.balance_card(balance="12,450.00", wallet_label="myFawry wallet •• 4521"),
        c.search_bar(),
        c.promo_card(
            badge="New",
            title="Get your Fawry Yellow Card",
            subtitle="Free delivery. Pay, save and split everywhere in Egypt.",
            cta_primary="Request card — free",
            cta_secondary="Add +",
            card_number="•• 4521",
            card_owner="AHMED M.",
        ),
        c.quick_pay_grid(QUICK_PAY_ITEMS),
        c.feature_grid("Do more with Fawry", FEATURE_CARDS),
        c.cashback_banner(
            text="50% cashback on first Yellow Card top-up",
            sub="Ends Sunday • Selected merchants",
        ),
        c.recent_payments("Recent payments", RECENT_PAYMENTS),
        c.bottom_nav(NAV_ITEMS, active="home"),
    ]
    return c.page(sections)


with gr.Blocks(title="Fawry Home") as demo:
    gr.HTML(build_home_html())

if __name__ == "__main__":
    demo.launch(css=CUSTOM_CSS)
