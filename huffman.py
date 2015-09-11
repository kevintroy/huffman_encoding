# Huffman's algorithm for variable-length encoding
# Takes a plaintext and returns a codebook together with the coded text

def huffman(plaintext):

    # helper function: construct the frequency table for the plaintext
    def frequency_table(plaintext):
        table = {}
        for char in plaintext:
            if char in table:
                table[char] += 1
            else:
                table[char] = 1
        return table


    # helper function: construct the graph from the bottom up
    # We will do this using a list of (gram, frequency, [children]) nodes
    # When first called, all nodes will be separated and have no children
    # Then we call recursively until all nodes are assembled into the tree
    def huffman_tree(nodes_list):
        # base case: all nodes have been combined into one tree, i.e. we're done
        if len(nodes_list) < 2:
            return nodes_list
        else:
            nodes_list.sort(key= lambda i: i[1], reverse = True)  #sort by frequency
            leaf_node0 = nodes_list.pop()  # take the two nodes with least frequency 
            leaf_node1 = nodes_list.pop()  # and combine them into a branch
            branch_node = (leaf_node0[0] + " or " + leaf_node1[0],
                           leaf_node0[1] + leaf_node1[1],
                           [leaf_node0, leaf_node1])

            return huffman_tree(nodes_list + [branch_node])
            
    # Helper function: take the binary tree and assign encodings to each node
    # When first called, pass empty string as the encoding
    # Each recursive call will add either "1" or "0" to the encoding
    def huffman_encoding(node, encoding):
        if not node[2]:                  # base case: no child nodes
            return [(node[0], encoding)]
        else:
            return huffman_encoding(node[2][0], encoding + "0") + \
                   huffman_encoding(node[2][1], encoding + "1")

    tree = huffman_tree([(k,v,[]) for(k,v) in frequency_table(plaintext).items()])[0]
    codetable = dict(huffman_encoding(tree, ""))
    codewords = tuple(codetable[char] for char in plaintext)

    return (codetable, codewords)



# test_dict_hw = {"5": 1, "4": 5, "3": 10, "2": 10, "1": 5, "0": 1}
# test_dict_tut1 = {"A": .24, "B": .35, "C": .21, "D": .13, "F": .07}
# test_dict_tut2 = {"alpha": .5, "beta": .125, "gamma": .25, "delta": .125}
# test_dict_ex1 = {"1": 74, "2": 387, "3": 360, "7": 54}
test_plaintext1 = """
a way a lone a last a loved a long the riverrun, past Eve and Adam's,
from swerve of shore to bend of bay, brings us by a commodius vicus
of recirculation back to Howth Castle and Environs"""
test_plaintext2 = """
My baloney has a first name, it's O-S-C-A-R.  My baloney has a second name,
it's M-E-Y-E-R."""
test_plaintext3 = """
My child and I hold hands on the way to school,
And when I leave him at the first-grade door
He cries a little but is brave; he does
Let go. My selfish tears remind me how
I cried before that door a life ago.
I may have had a hard time letting go.

Each fall the children must endure together
What every child also endures alone:
Learning the alphabet, the integers,
Three dozen bits and pieces of a stuff
So arbitrary, so peremptory,
That worlds invisible and visible

Bow down before it, as in Joseph’s dream
The sheaves bowed down and then the stars bowed down
Before the dreaming of a little boy.
That dream got him such hatred of his brothers
As cost the greater part of life to mend,
And yet great kindness came of it in the end.

II

A school is where they grind the grain of thought,
And grind the children who must mind the thought.
It may be those two grindings are but one,
As from the alphabet come Shakespeare’s Plays,
As from the integers comes Euler’s Law,
As from the whole, inseperably, the lives,

The shrunken lives that have not been set free
By law or by poetic phantasy.
But may they be. My child has disappeared
Behind the schoolroom door. And should I live
To see his coming forth, a life away,
I know my hope, but do not know its form

Nor hope to know it. May the fathers he finds
Among his teachers have a care of him
More than his father could. How that will look
I do not know, I do not need to know.
Even our tears belong to ritual.
But may great kindness come of it in the end."""
