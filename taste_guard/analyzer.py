"""
Content Quality Analyzer Module

Provides comprehensive analysis of text content quality including:
- Generic phrase detection
- Vocabulary diversity analysis
- Sentence structure variation
- Emotional engagement scoring
- Readability assessment
"""

import re
import math
from typing import Dict, List, Tuple, Any
from collections import Counter


class ContentAnalyzer:
    """Analyzes content quality and provides detailed metrics."""

    # Common generic phrases that make content feel "AI-generated"
    GENERIC_PHRASES = [
        "in the world of", "in today's world", "in the ever-changing",
        "it is important to note", "it should be noted", "it is worth noting",
        "as we all know", "as everyone knows", "it goes without saying",
        "at the end of the day", "when all is said and done",
        "in conclusion", "to sum up", "all in all", "overall",
        "delve into", "deep dive", "leverage", "synergy", "paradigm",
        "game changer", "think outside the box", "low hanging fruit",
        "moving forward", "going forward", "at this point in time",
        "due to the fact that", "in order to", "for the purpose of",
        "in the event that", "with regard to", "in relation to",
        "it is what it is", "the fact of the matter is",
        "needless to say", "without further ado",
        "let's get started", "let's dive in", "let's explore",
        "in this article", "in this blog post", "in this guide",
        "we will explore", "we will discuss", "we will look at",
        "fast-paced world", "rapidly evolving", "constantly changing",
        "digital age", "digital era", "modern world",
        "unlock your potential", "unleash your", "discover the power",
        "transform your", "revolutionize your", "supercharge your",
    ]

    # Weak modifiers that dilute meaning
    WEAK_MODIFIERS = [
        "very", "really", "quite", "rather", "pretty", "fairly",
        "somewhat", "kind of", "sort of", "basically", "literally",
        "actually", "essentially", "fundamentally", "ultimately",
    ]

    # Overused AI transition words
    OVERUSED_TRANSITIONS = [
        "furthermore", "moreover", "additionally", "consequently",
        "therefore", "thus", "hence", "nevertheless", "nonetheless",
        "however", "although", "whereas", "meanwhile", "subsequently",
    ]

    def __init__(self):
        self.generic_phrases = [p.lower() for p in self.GENERIC_PHRASES]
        self.weak_modifiers = [m.lower() for m in self.WEAK_MODIFIERS]
        self.overused_transitions = [t.lower() for t in self.OVERUSED_TRANSITIONS]

    def analyze(self, text: str) -> Dict[str, Any]:
        """
        Perform comprehensive content analysis.

        Args:
            text: The content to analyze

        Returns:
            Dictionary containing all analysis metrics
        """
        if not text or not text.strip():
            return self._empty_result()

        text_lower = text.lower()
        sentences = self._split_sentences(text)
        words = self._extract_words(text_lower)

        result = {
            "overall_score": 0.0,
            "generic_phrases": self._detect_generic_phrases(text_lower),
            "viversity_metrics": self._analyze_vocabulary_diversity(words),
            "sentence_variation": self._analyze_sentence_variation(sentences),
            "engagement_score": self._calculate_engagement(text, sentences, words),
            "readability": self._calculate_readability(text, sentences, words),
            "weak_modifiers": self._detect_weak_modifiers(text_lower),
            "transition_usage": self._analyze_transitions(text_lower),
            "suggestions": [],
        }

        result["overall_score"] = self._calculate_overall_score(result)
        result["suggestions"] = self._generate_suggestions(result)

        return result

    def _empty_result(self) -> Dict[str, Any]:
        """Return empty result for empty input."""
        return {
            "overall_score": 0.0,
            "generic_phrases": {"count": 0, "phrases": [], "density": 0.0},
            "viversity_metrics": {
                "unique_words": 0,
                "total_words": 0,
                "diversity_ratio": 0.0,
                "unique_bigrams": 0,
                "bigram_diversity": 0.0,
            },
            "sentence_variation": {
                "sentence_count": 0,
                "avg_length": 0.0,
                "length_variation": 0.0,
                "starting_patterns": [],
                "pattern_diversity": 0.0,
            },
            "engagement_score": {
                "score": 0.0,
                "active_voice_ratio": 0.0,
                "sensory_words": 0,
                "question_count": 0,
                "exclamation_count": 0,
            },
            "readability": {
                "flesch_reading_ease": 0.0,
                "flesch_kincaid_grade": 0.0,
                "avg_syllables_per_word": 0.0,
                "avg_words_per_sentence": 0.0,
            },
            "weak_modifiers": {"count": 0, "modifiers": [], "density": 0.0},
            "transition_usage": {"count": 0, "transitions": [], "density": 0.0},
            "suggestions": [],
        }

    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences."""
        # Simple sentence splitting
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]

    def _extract_words(self, text: str) -> List[str]:
        """Extract words from text."""
        words = re.findall(r'\b[a-z]+\b', text)
        return [w for w in words if len(w) > 1]

    def _detect_generic_phrases(self, text: str) -> Dict[str, Any]:
        """Detect generic phrases in text."""
        found = []
        for phrase in self.generic_phrases:
            count = text.count(phrase)
            if count > 0:
                found.append({"phrase": phrase, "count": count})

        total_count = sum(item["count"] for item in found)
        word_count = len(text.split())
        density = (total_count / word_count * 100) if word_count > 0 else 0.0

        return {
            "count": total_count,
            "phrases": found,
            "density": round(density, 2),
        }

    def _analyze_vocabulary_diversity(self, words: List[str]) -> Dict[str, Any]:
        """Analyze vocabulary diversity."""
        if not words:
            return {
                "unique_words": 0,
                "total_words": 0,
                "diversity_ratio": 0.0,
                "unique_bigrams": 0,
                "bigram_diversity": 0.0,
            }

        unique_words = len(set(words))
        total_words = len(words)
        diversity_ratio = unique_words / total_words if total_words > 0 else 0.0

        # Bigram analysis
        bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
        unique_bigrams = len(set(bigrams))
        bigram_diversity = unique_bigrams / len(bigrams) if bigrams else 0.0

        return {
            "unique_words": unique_words,
            "total_words": total_words,
            "diversity_ratio": round(diversity_ratio, 3),
            "unique_bigrams": unique_bigrams,
            "bigram_diversity": round(bigram_diversity, 3),
        }

    def _analyze_sentence_variation(self, sentences: List[str]) -> Dict[str, Any]:
        """Analyze sentence structure variation."""
        if not sentences:
            return {
                "sentence_count": 0,
                "avg_length": 0.0,
                "length_variation": 0.0,
                "starting_patterns": [],
                "pattern_diversity": 0.0,
            }

        lengths = [len(s.split()) for s in sentences]
        avg_length = sum(lengths) / len(lengths)

        # Calculate standard deviation for variation
        if len(lengths) > 1:
            variance = sum((l - avg_length) ** 2 for l in lengths) / len(lengths)
            length_variation = math.sqrt(variance)
        else:
            length_variation = 0.0

        # Analyze starting patterns (first 3 words)
        patterns = []
        for sent in sentences:
            words = sent.split()[:3]
            if words:
                pattern = " ".join(words).lower()
                patterns.append(pattern)

        pattern_counts = Counter(patterns)
        pattern_diversity = len(pattern_counts) / len(patterns) if patterns else 0.0

        return {
            "sentence_count": len(sentences),
            "avg_length": round(avg_length, 1),
            "length_variation": round(length_variation, 2),
            "starting_patterns": [{"pattern": p, "count": c} for p, c in pattern_counts.most_common(5)],
            "pattern_diversity": round(pattern_diversity, 3),
        }

    def _calculate_engagement(self, text: str, sentences: List[str], words: List[str]) -> Dict[str, Any]:
        """Calculate engagement score."""
        if not words:
            return {
                "score": 0.0,
                "active_voice_ratio": 0.0,
                "sensory_words": 0,
                "question_count": 0,
                "exclamation_count": 0,
            }

        # Sensory words
        sensory_words = [
            "see", "saw", "watch", "look", "gaze", "glance",
            "hear", "listen", "sound", "noise", "silent",
            "feel", "touch", "smooth", "rough", "soft", "hard",
            "smell", "scent", "aroma", "fragrance", "odor",
            "taste", "flavor", "sweet", "sour", "bitter", "spicy",
            "bright", "dark", "color", "vivid", "dull",
            "loud", "quiet", "whisper", "shout", "scream",
            "warm", "cold", "hot", "cool", "freezing",
        ]

        sensory_count = sum(1 for w in words if w in sensory_words)

        # Questions and exclamations
        question_count = text.count("?")
        exclamation_count = text.count("!")

        # Active voice estimation (simplified)
        passive_indicators = ["was", "were", "been", "being", "is", "are", "am"]
        passive_count = sum(1 for w in words if w in passive_indicators)
        active_voice_ratio = 1.0 - (passive_count / len(words) * 3) if words else 0.0
        active_voice_ratio = max(0.0, min(1.0, active_voice_ratio))

        # Calculate engagement score (0-100)
        score = 50.0  # Base score
        score += min(20, sensory_count * 2)  # Sensory words bonus
        score += min(15, question_count * 5)  # Questions bonus
        score += min(10, exclamation_count * 2)  # Exclamations bonus
        score += active_voice_ratio * 15  # Active voice bonus
        score = min(100.0, score)

        return {
            "score": round(score, 1),
            "active_voice_ratio": round(active_voice_ratio, 3),
            "sensory_words": sensory_count,
            "question_count": question_count,
            "exclamation_count": exclamation_count,
        }

    def _calculate_readability(self, text: str, sentences: List[str], words: List[str]) -> Dict[str, float]:
        """Calculate readability metrics."""
        if not sentences or not words:
            return {
                "flesch_reading_ease": 0.0,
                "flesch_kincaid_grade": 0.0,
                "avg_syllables_per_word": 0.0,
                "avg_words_per_sentence": 0.0,
            }

        def count_syllables(word: str) -> int:
            """Estimate syllable count."""
            word = word.lower()
            vowels = "aeiouy"
            count = 0
            prev_was_vowel = False
            for char in word:
                is_vowel = char in vowels
                if is_vowel and not prev_was_vowel:
                    count += 1
                prev_was_vowel = is_vowel
            if word.endswith("e"):
                count -= 1
            if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
                count += 1
            return max(1, count)

        total_syllables = sum(count_syllables(w) for w in words)
        avg_syllables = total_syllables / len(words)
        avg_words_per_sentence = len(words) / len(sentences)

        # Flesch Reading Ease
        flesch = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables)

        # Flesch-Kincaid Grade Level
        fk_grade = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables) - 15.59

        return {
            "flesch_reading_ease": round(flesch, 1),
            "flesch_kincaid_grade": round(fk_grade, 1),
            "avg_syllables_per_word": round(avg_syllables, 2),
            "avg_words_per_sentence": round(avg_words_per_sentence, 1),
        }

    def _detect_weak_modifiers(self, text: str) -> Dict[str, Any]:
        """Detect weak modifiers."""
        found = []
        for modifier in self.weak_modifiers:
            count = text.count(modifier)
            if count > 0:
                found.append({"modifier": modifier, "count": count})

        total_count = sum(item["count"] for item in found)
        word_count = len(text.split())
        density = (total_count / word_count * 100) if word_count > 0 else 0.0

        return {
            "count": total_count,
            "modifiers": found,
            "density": round(density, 2),
        }

    def _analyze_transitions(self, text: str) -> Dict[str, Any]:
        """Analyze transition word usage."""
        found = []
        for transition in self.overused_transitions:
            count = text.count(transition)
            if count > 0:
                found.append({"transition": transition, "count": count})

        total_count = sum(item["count"] for item in found)
        word_count = len(text.split())
        density = (total_count / word_count * 100) if word_count > 0 else 0.0

        return {
            "count": total_count,
            "transitions": found,
            "density": round(density, 2),
        }

    def _calculate_overall_score(self, result: Dict[str, Any]) -> float:
        """Calculate overall content quality score."""
        score = 100.0

        # Deduct for generic phrases
        generic_density = result["generic_phrases"]["density"]
        score -= generic_density * 5

        # Deduct for weak modifiers
        weak_density = result["weak_modifiers"]["density"]
        score -= weak_density * 3

        # Deduct for overused transitions
        transition_density = result["transition_usage"]["density"]
        score -= transition_density * 2

        # Vocabulary diversity bonus/penalty
        diversity = result["viversity_metrics"]["diversity_ratio"]
        if diversity < 0.3:
            score -= (0.3 - diversity) * 100
        elif diversity > 0.6:
            score += (diversity - 0.6) * 50

        # Sentence variation bonus/penalty
        pattern_diversity = result["sentence_variation"]["pattern_diversity"]
        if pattern_diversity < 0.3:
            score -= (0.3 - pattern_diversity) * 50

        # Engagement bonus
        engagement = result["engagement_score"]["score"]
        score += (engagement - 50) * 0.3

        return round(max(0.0, min(100.0, score)), 1)

    def _generate_suggestions(self, result: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate improvement suggestions."""
        suggestions = []

        # Generic phrases suggestions
        if result["generic_phrases"]["count"] > 0:
            phrases = result["generic_phrases"]["phrases"]
            top_phrases = [p["phrase"] for p in phrases[:3]]
            suggestions.append({
                "category": "generic_phrases",
                "severity": "high" if result["generic_phrases"]["count"] > 3 else "medium",
                "message": f"检测到 {result['generic_phrases']['count']} 个通用短语，如: {', '.join(top_phrases)}",
                "suggestion": "尝试用更具体的描述替换这些通用表达，使用独特的比喻或具体场景",
            })

        # Vocabulary diversity suggestions
        diversity = result["viversity_metrics"]["diversity_ratio"]
        if diversity < 0.4:
            suggestions.append({
                "category": "vocabulary",
                "severity": "high",
                "message": f"词汇多样性较低 ({diversity:.2f})，内容可能显得重复单调",
                "suggestion": "使用同义词替换重复词汇，引入专业术语或生动的形容词",
            })

        # Sentence variation suggestions
        pattern_diversity = result["sentence_variation"]["pattern_diversity"]
        if pattern_diversity < 0.4:
            suggestions.append({
                "category": "sentence_structure",
                "severity": "medium",
                "message": f"句子开头模式重复度较高 ({pattern_diversity:.2f})",
                "suggestion": "变换句子开头方式，使用不同的主语、副词或从句开头",
            })

        # Engagement suggestions
        engagement = result["engagement_score"]["score"]
        if engagement < 40:
            suggestions.append({
                "category": "engagement",
                "severity": "medium",
                "message": f"内容互动性较低 (得分: {engagement:.1f})",
                "suggestion": "增加感官描述、提问或感叹，使用主动语态增强表达力",
            })

        # Weak modifiers suggestions
        if result["weak_modifiers"]["count"] > 2:
            suggestions.append({
                "category": "weak_modifiers",
                "severity": "low",
                "message": f"发现 {result['weak_modifiers']['count']} 个弱化修饰词",
                "suggestion": "用更精确的词汇替代'非常'、'相当'等模糊修饰词",
            })

        # Transition suggestions
        if result["transition_usage"]["count"] > 3:
            suggestions.append({
                "category": "transitions",
                "severity": "low",
                "message": f"过渡词使用过于频繁 ({result['transition_usage']['count']} 次)",
                "suggestion": "减少'此外'、'因此'等过渡词，让段落自然衔接",
            })

        if not suggestions:
            suggestions.append({
                "category": "excellent",
                "severity": "info",
                "message": "内容质量优秀！未发现明显问题",
                "suggestion": "继续保持，可以尝试加入更多个人风格元素",
            })

        return suggestions
