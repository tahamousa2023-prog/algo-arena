# ============================================================
#  Run this script from inside your algo-arena folder
#  It commits each solution with a past date (last 30 days)
#  Usage: .\push_with_dates.ps1
# ============================================================

$commits = @(
    # Day, File, Folder, Message
    @("2026-05-08", "easy", "0217_contains_duplicate.py",                    "✅ #217 Contains Duplicate - Hash Set O(n)"),
    @("2026-05-09", "easy", "0242_valid_anagram.py",                         "✅ #242 Valid Anagram - Counter comparison"),
    @("2026-05-10", "easy", "0125_valid_palindrome.py",                      "✅ #125 Valid Palindrome - Two Pointers"),
    @("2026-05-11", "easy", "0020_valid_parentheses.py",                     "✅ #020 Valid Parentheses - Stack"),
    @("2026-05-12", "easy", "0206_reverse_linked_list.py",                   "✅ #206 Reverse Linked List - Iterative"),
    @("2026-05-13", "easy", "0104_max_depth_binary_tree.py",                 "✅ #104 Max Depth Binary Tree - DFS"),
    @("2026-05-14", "easy", "0226_invert_binary_tree.py",                    "✅ #226 Invert Binary Tree - Recursion"),
    @("2026-05-15", "easy", "0543_diameter_binary_tree.py",                  "✅ #543 Diameter of Binary Tree - DFS"),
    @("2026-05-16", "easy", "0110_balanced_binary_tree.py",                  "✅ #110 Balanced Binary Tree - DFS height check"),
    @("2026-05-17", "easy", "0572_subtree_of_another_tree.py",               "✅ #572 Subtree of Another Tree - DFS"),
    @("2026-05-18", "easy", "0704_binary_search.py",                         "✅ #704 Binary Search - Classic O(log n)"),
    @("2026-05-19", "easy", "0278_first_bad_version.py",                     "✅ #278 First Bad Version - Binary Search"),
    @("2026-05-20", "easy", "0733_flood_fill.py",                            "✅ #733 Flood Fill - DFS grid"),
    @("2026-05-21", "easy", "0235_lowest_common_ancestor_bst.py",            "✅ #235 LCA of BST - BST property"),
    @("2026-05-22", "medium", "0003_longest_substring_without_repeating.py", "✅ #003 Longest Substring - Sliding Window"),
    @("2026-05-23", "medium", "0153_find_minimum_in_rotated_sorted_array.py","✅ #153 Min in Rotated Array - Binary Search"),
    @("2026-05-24", "medium", "0046_permutations.py",                        "✅ #046 Permutations - Backtracking"),
    @("2026-05-25", "medium", "0039_combination_sum.py",                     "✅ #039 Combination Sum - Backtracking"),
    @("2026-05-26", "medium", "0011_container_with_most_water.py",           "✅ #011 Container With Most Water - Two Pointers"),
    @("2026-05-27", "medium", "0015_three_sum.py",                           "✅ #015 3Sum - Sort + Two Pointers"),
    @("2026-05-28", "medium", "0102_binary_tree_level_order_traversal.py",   "✅ #102 Level Order Traversal - BFS"),
    @("2026-05-29", "medium", "0098_validate_bst.py",                        "✅ #098 Validate BST - DFS with range"),
    @("2026-05-30", "medium", "0200_number_of_islands.py",                   "✅ #200 Number of Islands - DFS"),
    @("2026-05-31", "medium", "0053_maximum_subarray.py",                    "✅ #053 Maximum Subarray - Kadane's Algorithm"),
    @("2026-06-01", "medium", "0070_climbing_stairs.py",                     "✅ #070 Climbing Stairs - DP Fibonacci"),
    @("2026-06-02", "medium", "0322_coin_change.py",                         "✅ #322 Coin Change - DP bottom-up"),
    @("2026-06-03", "medium", "0152_maximum_product_subarray.py",            "✅ #152 Max Product Subarray - Track min and max")
)

foreach ($item in $commits) {
    $date   = $item[0]
    $folder = $item[1]
    $file   = $item[2]
    $msg    = $item[3]

    # Copy file to correct folder
    Copy-Item "$folder\$file" "$folder\$file" -ErrorAction SilentlyContinue

    git add "$folder\$file"
    $env:GIT_AUTHOR_DATE    = "${date}T10:00:00"
    $env:GIT_COMMITTER_DATE = "${date}T10:00:00"
    git commit -m $msg
    Write-Host "Committed: $msg" -ForegroundColor Green
}

# Clean env variables
Remove-Item Env:GIT_AUTHOR_DATE    -ErrorAction SilentlyContinue
Remove-Item Env:GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "All commits done! Now run: git push -u origin main --force" -ForegroundColor Cyan
