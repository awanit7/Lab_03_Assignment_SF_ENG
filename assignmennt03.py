class DataEntry:
    def __init__(self, p_id, start_time, priority):
        self.p_id = p_id
        self.start_time = start_time
        self.priority = priority

class DataSorter:
    def __init__(self, data):
        self.data = data
    
    def sort_by_p_id(self):
        return sorted(self.data, key=lambda x: x.p_id)
    
    def sort_by_start_time(self):
        return sorted(self.data, key=lambda x: x.start_time)
    
    def sort_by_priority(self):
        return sorted(self.data, key=lambda x: x.priority)

def print_table(data):
    print("{:<6} {:<20} {:<10}".format("P_ID", "Start Time", "Priority"))
    print("=" * 40)
    for entry in data:
        print("{:<6} {:<20} {:<10}".format(entry.p_id, entry.start_time, entry.priority))

def main():
    # Sample data creation
    data = [
        DataEntry(101, "2023-08-25 08:00:00", 3),
        DataEntry(102, "2023-08-25 09:30:00", 1),
        DataEntry(103, "2023-08-25 10:15:00", 2),
        # Add more data entries here
    ]
    
    sorter = DataSorter(data)
    
    while True:
        print("\nSorting Options:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 4:
            print("Exiting program.")
            break
        
        if choice == 1:
            sorted_data = sorter.sort_by_p_id()
        elif choice == 2:
            sorted_data = sorter.sort_by_start_time()
        elif choice == 3:
            sorted_data = sorter.sort_by_priority()
        else:
            print("Invalid sorting parameter")
            continue
        
        print("\nSorted Data:")
        print_table(sorted_data)

if __name__ == "__main__":
    main()
