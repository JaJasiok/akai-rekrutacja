import json, datetime, urllib.request


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        try:
            with open("ratios.json", "r") as f:
                ratios = json.load(f)
                f.close()
                for el in ratios:
                    if el["base_currency"] == self.base and el["target_currency"] == self.target and el["date_fetched"] == datetime.date.today():
                        return True
                    return False
        except FileNotFoundError:
            return False
        
    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        api = urllib.request.urlopen("http://api.exchangeratesapi.io/v1/latest?access_key=0a973ba584391a75aa1db2b50f505646")
        data = json.loads(api.read().decode())
        ratio = data["rates"][self.target] / data["rates"][self.base]
        self.save_ratio(ratio)

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        with open("ratios.json", "r+") as f:
            ratios = json.load(f)
            f.seek(0)
            for el in ratios:
                if el["base_currency"] == self.base and el["target_currency"] == self.target:
                    el["date_fetched"] = datetime.date.today()
                    el["ratio"] = ratio
                    json.dump(ratios, f, indent = 4, default = str)
                    f.close()
                    return
            ratios.append({"base_currency" : self.base, "target_currency" : self.target, "date_fetched" : datetime.date.today(), "ratio" : ratio})
            json.dump(ratios, f, indent = 4, default = str)
            f.close()

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        with open("ratios.json", "r") as f:
            ratios = json.load(f)
            for el in ratios:
                if el["base_currency"] == self.base and el["target_currency"] == self.target:
                    return(el["ratio"])
            
        
