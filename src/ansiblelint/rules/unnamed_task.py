"""Implementation of unnamed-task rule."""

# Copyright (c) 2016 Will Thames <will@thames.id.au>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from typing import TYPE_CHECKING, Any, Dict, Union

from ansiblelint.rules import AnsibleLintRule
from ansiblelint.utils import is_nested_task

if TYPE_CHECKING:
    from typing import Optional

    from ansiblelint.file_utils import Lintable


class TaskHasNameRule(AnsibleLintRule):
    """All tasks should be named."""

    id = "unnamed-task"
    description = (
        "All tasks should have a distinct name for readability "
        "and for ``--start-at-task`` to work"
    )
    severity = "MEDIUM"
    tags = ["idiom"]
    version_added = "historic"

    def matchtask(
        self, task: Dict[str, Any], file: "Optional[Lintable]" = None
    ) -> Union[bool, str]:
        # Ignore nonamed block/always/rescue
        return not (task.get("name") or is_nested_task(task))
