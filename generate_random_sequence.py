''' script to generate random sequences between 2 sequences '''
import random
from evol_config import SEQUENCE_A, SEQUENCE_B, NUM_EVOLUTION_STEPS


def generate_random_sequence(a,b,num=10):
    print("Starting sequence generation...")
    # Convert strings to lists to make them mutable
    a_list = list(a[1])
    b_list = list(b[1])
    sequence_len = len(a_list)
    random_sequences_evolution = [a]

    for i in range(num):
        evolved = False
        while not evolved:
            random_pos_to_mutate = random.randint(0,sequence_len-1)
            if a_list[random_pos_to_mutate] != b_list[random_pos_to_mutate]:
                a_list[random_pos_to_mutate] = b_list[random_pos_to_mutate]
                evolved = True
                break  
        current_sequence = ''.join(a_list)  # Convert back to string for display
        random_sequences_evolution.append((f'I{i}',current_sequence))
        if a_list == b_list:
            break

    # add b to the end of the list      
    random_sequences_evolution.append(b)
    return random_sequences_evolution

def create_fasta(path):
    with open(f"rand_evol_{path[0][0]}_{path[-1][0]}.fasta", "w") as f:
        for i, seq in enumerate(path):
            f.write(f">{seq[0]}\n{seq[1]}\n")

def main(a,b,num_seq_evolution=10):
    path = generate_random_sequence(a,b,num=num_seq_evolution)
    create_fasta(path)
    print(f"Random sequence generated and saved to rand_evol_{a[0]}_{b[0]}.fasta")

if __name__ == "__main__":
    main(a=SEQUENCE_A, b=SEQUENCE_B, num_seq_evolution=NUM_EVOLUTION_STEPS)