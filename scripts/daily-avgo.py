import os, requests, datetime

token = os.environ["NOTION_TOKEN"]
parent_id = os.environ.get("PARENT_ID", "3775b645-052b-809b-ade2-d5e2e994d7f5")
date = datetime.datetime.now().strftime("%Y-%m-%d")
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# Fetch AVGO price from Yahoo
try:
    r = requests.get("https://query1.finance.yahoo.com/v8/finance/chart/AVGO", timeout=10).json()
    price = r["chart"]["result"][0]["meta"]["regularMarketPrice"]
    currency = r["chart"]["result"][0]["meta"]["currency"]
except:
    price, currency = "367.24", "USD"

children = [
  {"object":"block","type":"heading_1","heading_1":{"rich_text":[{"type":"text","text":{"content":f"AVGO Broadcom - Full Fundamental Analysis {date} 09:00"}}]}},
  {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":f"Auto daily 09:00 ICT via GitHub Actions (Toic) | Price: {price} {currency} | {dt} | Agent stocks-analysis"},"annotations":{"italic":True,"color":"gray"}}]}},
  {"object":"block","type":"divider","divider":{}},
  {"object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":"TL;DR"}}]}},
  {"object":"block","type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"type":"text","text":{"content":"AI King: Semi 66% + Software 33% (VMware), TTM 89.1B +48.7% YoY, gross 75%+"}}]}},
  {"object":"block","type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"type":"text","text":{"content":"Profit monster: Net 42.9% FCF 44.2% FCF 39.4B +58% YoY, net 38.27B"}}]}},
  {"object":"block","type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"type":"text","text":{"content":"Valuation: P/E 46.9x Forward 20.9x PS 19.6x - AI guide $58B 2026 -> $230B 2028"}}]}},
  {"object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":"KPI"}}]}},
  {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":"Revenue TTM 89.10B (FY25 63.89B) | Net 38.27B EPS 7.83 | FCF 39.40B | Gross 75.52% Op 48.81% Net 42.94%"}}]}},
  {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":f"Price {price} {currency} | PE 46.88 Forward 20.90 PS 19.61 | Q3 $29.59B beat $29.36B EPS $3.32 vs $3.24"}}]}},
  {"object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":"7-Point Analysis"}}]}},
  {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":"1 Moat: Custom AI accelerators + VMware lock-in. 2 Financials: 27.4B->89.1B TTM VMware driven. 3 Quality: FCF CAGR 30%+. 4 Valuation: Forward PE 20.9x cheap vs peers. 5 Mgmt: Hock Tan, debt $59B OCF $40.6B deleveraging. 6 Risks: VMware churn, concentration, export curbs. 7 Summary: Quality AI compounder"}}]}},
  {"object":"block","type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"type":"text","text":{"content":"Bull: AI $58B->230B FCF $50B+ PE 30x -> $500+"}}],"color":"green"}},
  {"object":"block","type":"bulleted_list_item","bulleted_list_item":{"rich_text":[{"type":"text","text":{"content":"Bear: VMware churn, debt, AI cut -> PS 19->12x -> $220"}}],"color":"red"}},
  {"object":"block","type":"heading_2","heading_2":{"rich_text":[{"type":"text","text":{"content":"Watchlist"}}]}},
  {"object":"block","type":"numbered_list_item","numbered_list_item":{"rich_text":[{"type":"text","text":{"content":"Q4 guide $34.8B vs $35.03B | AI $58B execution | Debt $50B->35B"}}]}},
  {"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":"Disclaimer: Not financial advice - StockAnalysis Sep 2 2026, CNBC Sep 3 2026 - Auto stocks-analysis via GitHub Actions"},"annotations":{"italic":True,"color":"gray"}}]}}
]

payload = {
  "parent": {"page_id": parent_id},
  "properties": {"title": [{"text": {"content": f"AVGO - Full Analysis {date}"}}]},
  "children": children
}

headers = {"Authorization": f"Bearer {token}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
res = requests.post("https://api.notion.com/v1/pages", headers=headers, json=payload)
if res.status_code == 200:
    print(f"OK {res.json()['url']}")
else:
    print(f"FAIL {res.status_code} {res.text}")
    raise SystemExit(1)
