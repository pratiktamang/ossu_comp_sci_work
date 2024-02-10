# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import pdb


def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """

    """
     "bust"
     "b", and list = ['ust', 'sut', 'stu', 'uts', 'tus', 'tsu']
        ust => "ubst", "usbt", "ustb"
    """

    s = sequence
    if len(s) == 0:
        return []
    if len(s) <= 1:
        return [s]

    res = []

    for i in range(len(s)):
        char = s[i]
        remaining_chars = s[:i] + s[i + 1 :]

        for perm in get_permutations(remaining_chars):
            res.append(char + perm)
    return res


if __name__ == "__main__":
    print(get_permutations("a"))
    print(get_permutations("ab"))
    print(get_permutations("abc"))
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)
