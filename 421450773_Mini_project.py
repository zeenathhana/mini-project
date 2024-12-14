class WorstFitMemoryAllocation:
    def __init__(self, memory_blocks):  
        self.memory_blocks = memory_blocks  
        self.block_status = ["Free"] * len(memory_blocks)  
    def allocate(self, processes):
        allocations = [-1] * len(processes)  
        for i, process_size in enumerate(processes):
            worst_index = -1  

            
            for j, block_size in enumerate(self.memory_blocks):
                if block_size >= process_size:
                    if worst_index == -1 or block_size > self.memory_blocks[worst_index]:
                        worst_index = j

            
            if worst_index != -1:
                allocations[i] = worst_index
                self.memory_blocks[worst_index] -= process_size
                self.block_status[worst_index] = f"Allocated to Process {i + 1}"

        return allocations, self.memory_blocks, self.block_status


# Testing
if __name__ == "__main__":
 
    memory_blocks = [200, 100, 150, 70, 50]

    processes = [300, 150, 50]
    allocator = WorstFitMemoryAllocation(memory_blocks)

    
    allocations, final_memory_state, block_status = allocator.allocate(processes)

    print("Process Allocation Results:")
    for i, block_index in enumerate(allocations):
        if block_index != -1:
            print(f"Process {i + 1} (Size: {processes[i]} KB) -> Block {block_index + 1}")
        else:
            print(f"Process {i + 1} (Size: {processes[i]} KB) -> Not Allocated")

    
    print("\nFinal Memory State:")
    for i in range(len(final_memory_state)):
     block_size = final_memory_state[i]
     status = block_status[i]
     print(f"Block {i + 1}: {block_size} KB ({status})")



