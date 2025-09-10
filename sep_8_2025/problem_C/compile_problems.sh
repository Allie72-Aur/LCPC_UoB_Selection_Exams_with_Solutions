# Iterate over all folders starting with "No.{number}" in the current
# directory in order, write the contents of each "Problem_Statement.md"
# markdown file to a single "problems.md" file.

# Write a header to the file first.
echo -e "# Problem Statements\n" > problems.md

for dir in No.[0-9]*; do
    if [ -d "$dir" ]; then
        if [ -f "$dir/Problem_Statement.md" ]; then
            # Append a hash sign first, turning level 1 headers into level 2 headers
            echo -n "#" >> problems.md
            # Append the contents of the Problem_Statement.md file to problems.md
            cat -s "$dir/Problem_Statement.md" >> problems.md
            echo -e -n "\n" >> problems.md  # Add some spacing between problems
        else
            echo "Warning: $dir/Problem_Statement.md not found."
        fi
    fi
done
# Remove Extra newline at the end
sed -i '${/^$/d;}' problems.md