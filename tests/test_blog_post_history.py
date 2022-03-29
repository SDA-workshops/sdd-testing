import unittest
from unittest.mock import Mock

from blogpost import BlogPostHistory


class TestBlogPostHistory(unittest.TestCase):
    def test_change_title_should_change_title(self):
        expected_title = "New title"
        blogpost = BlogPostHistory("Example", "...")
        blogpost.save = Mock()

        blogpost.change_title(expected_title)

        title, desc = blogpost.get_properties()
        self.assertEqual(title, expected_title)
        blogpost.save.assert_called_once_with()

    def test_change_description_should_change_description(self):
        blogpost = BlogPostHistory("Example", "...")
        expected_description = "Some description"
        blogpost.save = Mock()

        blogpost.change_description(expected_description)

        title, desc = blogpost.get_properties()
        self.assertEqual(desc, expected_description)
        blogpost.save.assert_called_once_with()

    def test_change_title_should_raise_on_os_error(self):
        blogpost = BlogPostHistory("Example", "...")
        blogpost.save = Mock(side_effect=OSError)

        self.assertRaises(
            Exception, blogpost.change_title, "New title"
        )
