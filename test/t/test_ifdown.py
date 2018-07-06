import os

import pytest


class Test(object):

    @pytest.mark.skipif(bool(os.environ.get("CI")),
                        reason="Probably fails in CI")
    @pytest.mark.complete("ifdown ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("ifdown bash-completion ")
    def test_nonexistent(self, completion):
        assert not completion.list
