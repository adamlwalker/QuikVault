import json

with open("clients/apps/browser/src/manifest.json", "r", encoding="utf-8") as f:
    orig = json.load(f)

orig["name"] = "QuikVault"
orig["short_name"] = "QuikVault"
orig["author"] = "Bitwarden® community"
orig["homepage_url"] = "https://github.com/adamlwalker/QuikVault"
orig["__firefox__browser_specific_settings"]["gecko"][
    "id"
] = "{e24f0f46-f3ba-4d4e-a40d-2eee2aee41b7}"
orig["description"] = (
    "QuikVault is an exclusive build of the popular open source password manager"
)
orig["icons"] = {
    "16": "images/icon16_sunset.png",
    "32": "images/icon32_sunset.png",
    "48": "images/icon48_sunset.png",
    "96": "images/icon96_sunset.png",
    "128": "images/icon128_sunset.png",
    "256": "images/icon256_sunset.png",
    "512": "images/icon512_sunset.png",
}

if len(orig["description"]) > 132:
    raise ValueError("Description too long")

with open("clients/apps/browser/src/manifest.json", "w", encoding="utf-8") as f:
    json.dump(orig, f, indent=2)
    print("Wrote manifest.json")
