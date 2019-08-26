#!/usr/bin/env fish
pandoc -s --toc --toc-depth=3 -o index.html -c pandoc.css -f markdown games.md dataset.md otherFiles.md gameImplementation.md