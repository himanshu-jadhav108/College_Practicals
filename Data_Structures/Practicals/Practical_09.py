# Experiment No:- 9
# Name :- Himanshu H. Jadhav
# Roll No:- 27
# Batch :- SE-2
# Graph Representation for Flight Paths

class FlightGraph:
    def __init__(self, num_cities):  
        self.graph = {}  
        self.num_cities = num_cities

    def add_flight(self, city_a, city_b, time):
        """Adds a flight between two cities with given travel time."""
        # Add city_a if not present
        if city_a not in self.graph:
            self.graph[city_a] = []
        # Add city_b if not present
        if city_b not in self.graph:
            self.graph[city_b] = []
        
        # Add the flight (assuming bidirectional connection)
        self.graph[city_a].append((city_b, time))
        self.graph[city_b].append((city_a, time))

    def display_graph(self):
        """Displays the adjacency list representation of the graph."""
        if not self.graph:
            print("Graph is empty. Please add flights first.")
            return

        print("\nFlight Graph (Adjacency List):")
        for city, connections in self.graph.items():
            connections_str = ", ".join([f"{dest} ({time} hrs)" for dest, time in connections])
            print(f"{city} -> {connections_str}")


def main():
    flight_graph = None  

    while True:
        print("\n=== Flight Graph Menu ===")
        print("1. Create Graph using Adjacency List")
        print("2. Display Graph")
        print("3. Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            num_cities = int(input("Enter number of cities: "))
            num_flights = int(input("Enter number of flights: "))
            flight_graph = FlightGraph(num_cities)

            for _ in range(num_flights):
                city_a = input("Enter Source City: ").strip()
                city_b = input("Enter Destination City: ").strip()
                try:
                    time = int(input("Enter Time required (in hrs): "))
                except ValueError:
                    print("Invalid time! Skipping this flight.")
                    continue
                flight_graph.add_flight(city_a, city_b, time)

        elif choice == 2:
            if flight_graph:
                flight_graph.display_graph()
            else:
                print("Graph not created yet. Please create a graph first.")

        elif choice == 3:
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__== "__main__":
    main()