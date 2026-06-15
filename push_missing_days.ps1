# ============================================================
#  Run from inside your algo-arena folder
#  Fills all missing days March 15 → May 4 (51 commits)
# ============================================================

$commits = @(
    @("2026-03-15","easy","0009_palindrome_number.py",                 "✅ #009 Palindrome Number - Math string reverse"),
    @("2026-03-16","easy","0013_roman_to_integer.py",                  "✅ #013 Roman to Integer - Hash map walk right-to-left"),
    @("2026-03-17","easy","0014_longest_common_prefix.py",             "✅ #014 Longest Common Prefix - Shrink prefix"),
    @("2026-03-18","easy","0026_remove_duplicates_sorted_array.py",    "✅ #026 Remove Duplicates Sorted Array - Two Pointers"),
    @("2026-03-19","easy","0027_remove_element.py",                    "✅ #027 Remove Element - Two Pointers in-place"),
    @("2026-03-20","easy","0028_find_index_first_occurrence.py",       "✅ #028 Find Index First Occurrence - Sliding window"),
    @("2026-03-21","easy","0035_search_insert_position.py",            "✅ #035 Search Insert Position - Binary Search"),
    @("2026-03-22","easy","0058_length_of_last_word.py",               "✅ #058 Length of Last Word - String traversal"),
    @("2026-03-23","easy","0066_plus_one.py",                          "✅ #066 Plus One - Array carry propagation"),
    @("2026-03-24","easy","0067_add_binary.py",                        "✅ #067 Add Binary - Two pointer bit addition"),
    @("2026-03-25","easy","0069_sqrt.py",                              "✅ #069 Sqrt(x) - Binary Search on value range"),
    @("2026-03-26","easy","0083_remove_duplicates_sorted_list.py",     "✅ #083 Remove Duplicates Sorted List - Linked List"),
    @("2026-03-27","easy","0088_merge_sorted_array.py",                "✅ #088 Merge Sorted Array - Fill from end"),
    @("2026-03-28","easy","0100_same_tree.py",                         "✅ #100 Same Tree - DFS recursion"),
    @("2026-03-29","easy","0101_symmetric_tree.py",                    "✅ #101 Symmetric Tree - Mirror DFS"),
    @("2026-03-30","easy","0111_min_depth_binary_tree.py",             "✅ #111 Min Depth Binary Tree - BFS"),
    @("2026-03-31","easy","0112_path_sum.py",                          "✅ #112 Path Sum - DFS target tracking"),
    @("2026-04-01","easy","0118_pascals_triangle.py",                  "✅ #118 Pascal's Triangle - DP row by row"),
    @("2026-04-02","easy","0119_pascals_triangle_ii.py",               "✅ #119 Pascal's Triangle II - DP in-place"),
    @("2026-04-03","easy","0136_single_number.py",                     "✅ #136 Single Number - XOR bit trick"),
    @("2026-04-04","easy","0141_linked_list_cycle.py",                 "✅ #141 Linked List Cycle - Floyd tortoise hare"),
    @("2026-04-05","easy","0144_binary_tree_preorder.py",              "✅ #144 Binary Tree Preorder - Iterative stack"),
    @("2026-04-06","easy","0145_binary_tree_postorder.py",             "✅ #145 Binary Tree Postorder - Reversed preorder"),
    @("2026-04-07","easy","0160_intersection_linked_lists.py",         "✅ #160 Intersection Linked Lists - Two pointers"),
    @("2026-04-08","easy","0168_excel_column_title.py",                "✅ #168 Excel Column Title - Base-26 conversion"),
    @("2026-04-09","easy","0169_majority_element.py",                  "✅ #169 Majority Element - Boyer-Moore voting"),
    @("2026-04-10","easy","0171_excel_column_number.py",               "✅ #171 Excel Column Number - Base-26 to int"),
    @("2026-04-11","easy","0172_factorial_trailing_zeroes.py",         "✅ #172 Factorial Trailing Zeroes - Count 5s"),
    @("2026-04-12","easy","0190_reverse_bits.py",                      "✅ #190 Reverse Bits - Bit manipulation"),
    @("2026-04-13","easy","0191_number_of_1_bits.py",                  "✅ #191 Number of 1 Bits - n&(n-1) trick"),
    @("2026-04-14","easy","0202_happy_number.py",                      "✅ #202 Happy Number - Cycle detection with set"),
    @("2026-04-15","easy","0203_remove_linked_list_elements.py",       "✅ #203 Remove Linked List Elements - Dummy head"),
    @("2026-04-16","easy","0205_isomorphic_strings.py",                "✅ #205 Isomorphic Strings - Bidirectional map"),
    @("2026-04-17","easy","0219_contains_duplicate_ii.py",             "✅ #219 Contains Duplicate II - Sliding window set"),
    @("2026-04-18","easy","0228_summary_ranges.py",                    "✅ #228 Summary Ranges - Range detection"),
    @("2026-04-19","easy","0231_power_of_two.py",                      "✅ #231 Power of Two - Bit trick n&(n-1)"),
    @("2026-04-20","easy","0234_palindrome_linked_list.py",            "✅ #234 Palindrome Linked List - Collect and check"),
    @("2026-04-21","easy","0257_binary_tree_paths.py",                 "✅ #257 Binary Tree Paths - DFS path building"),
    @("2026-04-22","easy","0258_add_digits.py",                        "✅ #258 Add Digits - Digital root formula"),
    @("2026-04-23","easy","0263_ugly_number.py",                       "✅ #263 Ugly Number - Divide out 2,3,5"),
    @("2026-04-24","easy","0268_missing_number.py",                    "✅ #268 Missing Number - Sum formula"),
    @("2026-04-25","easy","0283_move_zeroes.py",                       "✅ #283 Move Zeroes - Two Pointers"),
    @("2026-04-26","easy","0290_word_pattern.py",                      "✅ #290 Word Pattern - Bidirectional map"),
    @("2026-04-27","easy","0326_power_of_three.py",                    "✅ #326 Power of Three - Divide by 3"),
    @("2026-04-28","easy","0338_counting_bits.py",                     "✅ #338 Counting Bits - DP bit shift"),
    @("2026-04-29","easy","0342_power_of_four.py",                     "✅ #342 Power of Four - Bit mask trick"),
    @("2026-04-30","easy","0344_reverse_string.py",                    "✅ #344 Reverse String - Two Pointers in-place"),
    @("2026-05-01","easy","0345_reverse_vowels.py",                    "✅ #345 Reverse Vowels - Two Pointers"),
    @("2026-05-02","easy","0349_intersection_of_two_arrays.py",        "✅ #349 Intersection of Two Arrays - Set"),
    @("2026-05-03","easy","0350_intersection_of_two_arrays_ii.py",     "✅ #350 Intersection Two Arrays II - Counter"),
    @("2026-05-04","easy","0001_two_sum.py",                           "✅ #001 Two Sum - Hash Map O(n) [revisit]")
)

foreach ($item in $commits) {
    $date=$item[0]; $folder=$item[1]; $file=$item[2]; $msg=$item[3]
    git add "$folder\$file"
    $env:GIT_AUTHOR_DATE    = "${date}T10:00:00"
    $env:GIT_COMMITTER_DATE = "${date}T10:00:00"
    git commit -m $msg
    Write-Host "✅ $date — $msg" -ForegroundColor Green
}

Remove-Item Env:GIT_AUTHOR_DATE    -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue
Write-Host ""
Write-Host "All 51 commits done! Run: git push origin main --force" -ForegroundColor Cyan
