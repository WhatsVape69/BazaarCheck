import requests, json, sys
source = requests.get("https://api.hypixel.net/skyblock/bazaar?key=XXXX").json()
quick_status_list = []
#for p in source["products"]:
#  quick_status_list.append(source["products"][p]["quick_status"])

for p in source["products"]:
  if p == "LOG_2:1":
    source["products"][p]["quick_status"]["productId"] = "Dark Oak Wood"
  if p == "RAW_FISH:1":
    source["products"][p]["quick_status"]["productId"] = "Raw Salmon"
  if p == "LOG:3":
    source["products"][p]["quick_status"]["productId"] = "Jungle Wood"
  if p == "RAW_FISH:2":
    source["products"][p]["quick_status"]["productId"] = "Clownfish"
  if p == "RAW_FISH:3":
    source["products"][p]["quick_status"]["productId"] = "Pufferfish"
  if p == "LOG:1":
    source["products"][p]["quick_status"]["productId"] = "Spruce Wood"
  if p == "LOG:2":
    source["products"][p]["quick_status"]["productId"] = "Acacia Wood"
  if p == "INK_SACK:3":
    source["products"][p]["quick_status"]["productId"] = "Cocoa Beans"
  if p == "INK_SACK:4":
    source["products"][p]["quick_status"]["productId"] = "Lapis Lazuli"
  if p == "LOG":
    source["products"][p]["quick_status"]["productId"] = "Oak Wood"
  if p == "NETHER_STALK":
    source["products"][p]["quick_status"]["productId"] = "Nether Wart"
  if p == "BROWN_MUSHROOM":
    source["products"][p]["quick_status"]["productId"] = "Brown Mushroom"
  if p == "SPOOKY_SHARD":
    source["products"][p]["quick_status"]["productId"] = "Spooky Shard"
  if p == "TARANTULA_WEB":
    source["products"][p]["quick_status"]["productId"] = "Tarantula Web"
  if p == "CARROT_ITEM":
    source["products"][p]["quick_status"]["productId"] = "Carrot"
  if p == "ENCHANTED_POTATO":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Potato"
  if p == "EXP_BOTTLE":
    source["products"][p]["quick_status"]["productId"] = "Experience Bottle"
  if p == "ENCHANTED_SLIME_BALL":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Slime Ball"
  if p == "ENCHANTED_GOLDEN_CARROT":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Golden Carrot"
  if p == "ENCHANTED_RED_MUSHROOM":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Red Mushroom"
  if p == "ENCHANTED_RABBIT_HIDE":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Rabbit Hide"
  if p == "ENCHANTED_BIRCH_LOG":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Birch Log"
  if p == "ENCHANTED_GUNPOWDER":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Gunpowder"
  if p == "ENCHANTED_MELON":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Melon"
  if p == "ENCHANTED_SUGAR":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Sugar"
  if p == "CACTUS":
    source["products"][p]["quick_status"]["productId"] = "Cactus"
  if p == "ENCHANTED_BLAZE_ROD":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Blaze Rod"
  if p == "ENCHANTED_CAKE":
    source["products"][p]["quick_status"]["productId"] = "Enchanted Cake"
  if p == "PUMPKIN":
    source["products"][p]["quick_status"]["productId"] = "Pumpkin"
  quick_status_list.append(source["products"][p]["quick_status"])


print("Done!")

original_stdout = sys.stdout

print("Saved to Bazaar.txt")
print("Or, you can access it here!")
print(json.dumps(quick_status_list, indent=1))

with open("bazaar.txt","w") as f:
    sys.stdout = f
    print("===============================================")
    print(json.dumps(quick_status_list, indent=1))
    print("===================== END =====================")
    sys.stdout = original_stdout
