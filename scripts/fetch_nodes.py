import requests, base64, re, os

# 免费订阅源地址（完整 9 个）
sub_sources = [
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml",
    "https://raw.githubusercontent.com/adiwzx/freenode/main/adispeed.txt",
    "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/mix",
    "https://raw.githubusercontent.com/pojiezhiyuanjun/freev2/master/0827.txt",
    "https://raw.githubusercontent.com/zyfxz/V2Ray/master/0827.txt",
    "https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/master/v2ray.txt",
    "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt"
]

def fetch_sub(url):
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            return res.text
    except:
        return ""
    return ""

all_nodes = []

for url in sub_sources:
    data = fetch_sub(url)
    if not data:
        continue
    try:
        decoded = base64.b64decode(data).decode("utf-8")
        all_nodes += decoded.strip().splitlines()
    except:
        lines = re.findall(r'(vmess://[^\s]+|ss://[^\s]+|trojan://[^\s]+|vless://[^\s]+)', data)
        all_nodes += lines

all_nodes = list(set(all_nodes))
final_nodes = all_nodes[:300]

os.makedirs("output", exist_ok=True)
with open("output/ios.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(final_nodes))

print(f"✅ 收集完成，共输出 {len(final_nodes)} 个节点，保存到 output/ios.txt")
