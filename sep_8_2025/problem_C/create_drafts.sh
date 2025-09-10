# Iterate over each folder starting with "No.{number}" in the current directory
# For each folder, create a draft file named "solution_draft.md" inside it
# Then copy the content of "Problem_Statement.md" into the newly created draft file
for dir in No.[0-9]*; do
    if [ -d "$dir" ]; then
        draft_file="$dir/solution_draft.md"
        # If draft file already exists, skip iteration
        if [ -f "$draft_file" ]; then
            echo "Draft file already exists: $draft_file"
            continue
        fi
        # Create the draft file and copy content
        echo "Create draft file: $draft_file"
        touch "$draft_file"
        cp "$dir/Problem_Statement.md" "$draft_file" --verbose
    fi
done