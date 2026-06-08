"""
Unit tests for ContentAnalyzer
"""

import pytest
from taste_guard.analyzer import ContentAnalyzer


class TestContentAnalyzer:
    """Test suite for ContentAnalyzer."""

    @pytest.fixture
    def analyzer(self):
        """Create analyzer instance."""
        return ContentAnalyzer()

    def test_empty_text(self, analyzer):
        """Test analyzing empty text."""
        result = analyzer.analyze("")
        assert result["overall_score"] == 0.0
        assert result["generic_phrases"]["count"] == 0

    def test_generic_phrases_detection(self, analyzer):
        """Test generic phrase detection."""
        text = "In today's world, we need to leverage synergy and think outside the box."
        result = analyzer.analyze(text)
        assert result["generic_phrases"]["count"] > 0

    def test_vocabulary_diversity(self, analyzer):
        """Test vocabulary diversity calculation."""
        text = "The quick brown fox jumps over the lazy dog."
        result = analyzer.analyze(text)
        vocab = result["viversity_metrics"]
        assert vocab["total_words"] > 0
        assert vocab["unique_words"] > 0
        assert 0.0 <= vocab["diversity_ratio"] <= 1.0

    def test_engagement_score(self, analyzer):
        """Test engagement score calculation."""
        text = "Can you see the bright colors? Feel the warm sunshine!"
        result = analyzer.analyze(text)
        engage = result["engagement_score"]
        assert engage["score"] > 0
        assert engage["question_count"] == 1
        assert engage["exclamation_count"] == 1
        assert engage["sensory_words"] > 0

    def test_readability(self, analyzer):
        """Test readability metrics."""
        text = "The cat sat on the mat. It was a sunny day."
        result = analyzer.analyze(text)
        read = result["readability"]
        assert read["flesch_reading_ease"] > 0
        assert read["avg_words_per_sentence"] > 0

    def test_weak_modifiers(self, analyzer):
        """Test weak modifier detection."""
        text = "It was very good and really quite interesting."
        result = analyzer.analyze(text)
        assert result["weak_modifiers"]["count"] > 0

    def test_suggestions_generation(self, analyzer):
        """Test suggestions generation."""
        text = "In today's world, it is very important to note that we must leverage synergy."
        result = analyzer.analyze(text)
        assert len(result["suggestions"]) > 0

    def test_high_quality_content(self, analyzer):
        """Test high quality content gets good score."""
        text = (
            "The aurora borealis painted the Arctic sky in vivid emerald waves. "
            "Local Inuit elders shared stories passed down through generations, "
            "their voices carrying wisdom across the frozen tundra. "
            "What secrets does the ice hold beneath its crystalline surface?"
        )
        result = analyzer.analyze(text)
        assert result["overall_score"] > 60

    def test_low_quality_content(self, analyzer):
        """Test low quality content gets poor score."""
        text = (
            "In today's world, it is important to note that we need to leverage synergy. "
            "Furthermore, we must think outside the box and delve into the paradigm. "
            "Moreover, it is very important to understand that we need to move forward."
        )
        result = analyzer.analyze(text)
        assert result["overall_score"] < 50


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
