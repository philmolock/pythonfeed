feedList = ['Bing_LIA_Product_Inventory_00.txt','Bing_LIA_Product_Inventory_01.txt','Bing_LIA_Product_Inventory_02.txt']
oldHeader = "retailstoreid"
newHeader = "storecode"

for feed in feedList:
    print(f"[{feed}]\tOpening Feed...")
    with open(feed, 'r') as feedFile:
        print(f"[{feed}]\tFeed Opened...")
        lines = feedFile.readlines()
        print(f"[{feed}]\tReplacing {oldHeader} with {newHeader}...")
        lines[0] = lines[0].replace(oldHeader, newHeader)
        if (feed != feedList[2]):
            print(f"[{feed}]\tFeed header adjusted, moving on to next file...\n")

    with open(feed, "w") as feedFile:
        feedFile.writelines(lines)


print("\nFinished!\n")
input("Please hit any key to exit...")
