import pandas as pd
from final_project.place import Place
from final_project.host import Host


class City:
    def __init__(self, size, area_rates):
        self.size = size
        self.area_rates = area_rates
        self.step = 0

    def initialize(self):
        self.places = []
        for pid in range(self.size * self.size):
            place = Place(place_id=pid, host_id=pid, city=self)
            place.setup()
            self.places.append(place)

        self.hosts = []
        for place in self.places:
            host = Host(host_id=place.host_id, place=place, city=self)
            self.hosts.append(host)

    def approve_bids(self, bids):
        if not bids:
            return []

        df_bids = pd.DataFrame(bids).sort_values(by='spread', ascending=False)

        approved = []
        buyers_done = set()
        places_sold = set()

        for _, row in df_bids.iterrows():
            buyer_id = int(row['buyer_id'])
            place_id = int(row['place_id'])

            if buyer_id not in buyers_done and place_id not in places_sold:
                approved.append(row.to_dict())
                buyers_done.add(buyer_id)
                places_sold.add(place_id)

        return approved

    def execute_transactions(self, transactions):
        for tx in transactions:
            buyer = self.hosts[int(tx['buyer_id'])]
            seller = self.hosts[int(tx['seller_id'])]
            place = self.places[int(tx['place_id'])]
            bid_price = tx['bid_price']

            buyer.profits -= bid_price
            seller.profits += bid_price
            buyer.assets.add(place.place_id)
            seller.assets.remove(place.place_id)

            place.host_id = buyer.host_id
            place.price[self.step] = bid_price

    def clear_market(self):
        all_bids = []
        for host in self.hosts:
            all_bids.extend(host.make_bids())

        approved = self.approve_bids(all_bids)
        if approved:
            self.execute_transactions(approved)
        return approved

    def iterate(self):
        self.step += 1
        for place in self.places:
            place.update_occupancy()
        for host in self.hosts:
            host.update_profits()
        return self.clear_market()
