class FlightGraph:
    def __init__(self, num_cities):
        self.graph = {}  # Adjacency list representation
        self.num_cities = num_cities

    def add_flight(self, city_a, city_b, time):
        if not city_a or not city_b or not isinstance(time, (int, float)) or time < 0:
            print("Invalid input: City names cannot be empty and time must be a positive number")
            return
            
        if city_a not in self.graph:
            self.graph[city_a] = []
        if city_b not in self.graph:
            self.graph[city_b] = []
        
        self.graph[city_a].append((city_b, time))
        self.graph[city_b].append((city_a, time))  # Assuming bidirectional flights

    def display_graph(self):
        print("Flight Graph:")
        for city in self.graph:
            print(f"{city} -> {self.graph[city]}")

if __name__ == "__main__":
    while True:
        print("\nMenu")
        print("1. Create Graph using adjacency List")
        print("2. Display Graph")
        print("3. Exit")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            num_cities = int(input("No of Cities? "))
            num_flights = int(input("No of Flights? "))
            flight_graph = FlightGraph(num_cities)

            for _ in range(num_flights):
                city_a = input("Enter Source City: ")
                city_b = input("Enter Destination City: ")
                time = int(input("Enter Time required: "))
                flight_graph.add_flight(city_a, city_b, time)

        elif choice == 2:
            if 'flight_graph' in locals():
                flight_graph.display_graph()
            else:
                print("Graph not created yet. Please create a graph first.")

        elif choice == 3:
            break
        else:
            print("Invalid Choice! Try Again.")
