"""
TasteGuard CLI Interface

Provides an intuitive command-line interface for content quality analysis
with rich formatting and colorful output.
"""

import sys
import json
import click
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.tree import Tree
from rich import box

from .analyzer import ContentAnalyzer
from . import __version__


console = Console()


def print_banner():
    """Print application banner."""
    banner = """
╭─────────────────────────────────────────────╮
│                                             │
│   🛡️  TasteGuard - AI Content Guardian     │
│                                             │
│   Evaluate & Optimize Content Quality       │
│                                             │
╰─────────────────────────────────────────────╯
    """
    console.print(banner, style="bold cyan")


def get_quality_color(score: float) -> str:
    """Get color based on quality score."""
    if score >= 80:
        return "green"
    elif score >= 60:
        return "yellow"
    elif score >= 40:
        return "orange3"
    else:
        return "red"


def get_severity_style(severity: str) -> str:
    """Get style for severity level."""
    styles = {
        "high": "bold red",
        "medium": "bold yellow",
        "low": "bold blue",
        "info": "bold green",
    }
    return styles.get(severity, "white")


@click.group(invoke_without_command=True)
@click.version_option(version=__version__, prog_name="taste-guard")
@click.pass_context
def cli(ctx):
    """🛡️ TasteGuard - AI Content Quality Guardian

    Analyze and optimize your AI-generated content for uniqueness,
    engagement, and quality. Stop generic "AI slop" in its tracks!
    """
    if ctx.invoked_subcommand is None:
        print_banner()
        console.print("\n[bold]用法:[/bold] taste-guard analyze [OPTIONS] [TEXT/FILE]")
        console.print("\n[bold]命令:[/bold]")
        console.print("  analyze    分析内容质量")
        console.print("  compare    比较两段内容")
        console.print("  optimize   获取优化建议")
        console.print("\n[bold]选项:[/bold]")
        console.print("  --help     显示帮助信息")
        console.print("\n[dim]示例: taste-guard analyze \"Your text here...\"[/dim]")


@cli.command()
@click.argument("content", required=False)
@click.option("--file", "-f", type=click.Path(exists=True), help="从文件读取内容")
@click.option("--json", "output_json", is_flag=True, help="以JSON格式输出")
@click.option("--verbose", "-v", is_flag=True, help="显示详细分析")
def analyze(content: Optional[str], file: Optional[str], output_json: bool, verbose: bool):
    """📊 分析内容质量

    分析文本内容的整体质量，包括通用短语检测、词汇多样性、
    句子结构变化和互动性评分。

    示例:
        taste-guard analyze "Your text here..."
        taste-guard analyze -f article.txt --verbose
    """
    if file:
        try:
            content = Path(file).read_text(encoding="utf-8")
        except Exception as e:
            console.print(f"[red]读取文件失败: {e}[/red]")
            sys.exit(1)
    elif not content:
        # Try to read from stdin
        if not sys.stdin.isatty():
            content = sys.stdin.read()
        else:
            console.print("[red]错误: 请提供文本内容或使用 --file 选项[/red]")
            sys.exit(1)

    analyzer = ContentAnalyzer()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        progress.add_task(description="🔍 正在分析内容质量...", total=None)
        result = analyzer.analyze(content)

    if output_json:
        console.print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # Display results
    _display_analysis_result(result, verbose)


def _display_analysis_result(result: dict, verbose: bool):
    """Display analysis result in rich format."""
    score = result["overall_score"]
    color = get_quality_color(score)

    # Overall Score Panel
    score_text = f"""
[bold {color}]整体质量评分: {score}/100[/bold {color}]

{"🌟 优秀" if score >= 80 else "👍 良好" if score >= 60 else "⚠️ 一般" if score >= 40 else "❌ 需改进"} - {"内容质量出色，独特性强" if score >= 80 else "内容质量不错，仍有提升空间" if score >= 60 else "内容较为普通，建议优化" if score >= 40 else "内容质量问题较多，需要大幅改进"}
    """
    console.print(Panel(score_text, title="📊 分析结果", border_style=color))

    # Metrics Table
    table = Table(title="📈 详细指标", box=box.ROUNDED)
    table.add_column("指标", style="cyan", no_wrap=True)
    table.add_column("数值", style="white")
    table.add_column("评价", style="dim")

    # Generic phrases
    generic = result["generic_phrases"]
    generic_status = "✅ 良好" if generic["count"] == 0 else f"⚠️ 发现 {generic['count']} 个"
    table.add_row(
        "通用短语",
        f"{generic['count']} 个 (密度: {generic['density']}%)",
        generic_status,
    )

    # Vocabulary diversity
    vocab = result["viversity_metrics"]
    vocab_status = "✅ 丰富" if vocab["diversity_ratio"] > 0.5 else "⚠️ 偏低"
    table.add_row(
        "词汇多样性",
        f"{vocab['diversity_ratio']:.2f} ({vocab['unique_words']}/{vocab['total_words']})",
        vocab_status,
    )

    # Sentence variation
    sent = result["sentence_variation"]
    sent_status = "✅ 丰富" if sent["pattern_diversity"] > 0.5 else "⚠️ 偏低"
    table.add_row(
        "句子变化度",
        f"{sent['pattern_diversity']:.2f} ({sent['sentence_count']} 句)",
        sent_status,
    )

    # Engagement
    engage = result["engagement_score"]
    engage_status = "✅ 高" if engage["score"] > 60 else "⚠️ 一般"
    table.add_row(
        "互动性评分",
        f"{engage['score']:.1f}/100",
        engage_status,
    )

    # Readability
    read = result["readability"]
    table.add_row(
        "可读性 (Flesch)",
        f"{read['flesch_reading_ease']:.1f}",
        "📖 参考值",
    )

    console.print(table)

    # Suggestions
    if result["suggestions"]:
        console.print("\n[bold]💡 优化建议[/bold]")
        for i, suggestion in enumerate(result["suggestions"], 1):
            severity_style = get_severity_style(suggestion["severity"])
            console.print(f"\n[{severity_style}]{i}. {suggestion['message']}[/{severity_style}]")
            console.print(f"   [dim]💭 建议: {suggestion['suggestion']}[/dim]")

    # Verbose details
    if verbose:
        console.print("\n[bold]🔍 详细检测信息[/bold]")

        if result["generic_phrases"]["phrases"]:
            console.print("\n[bold red]检测到的通用短语:[/bold red]")
            for phrase in result["generic_phrases"]["phrases"]:
                console.print(f"  • \"{phrase['phrase']}\" (出现 {phrase['count']} 次)")

        if result["weak_modifiers"]["modifiers"]:
            console.print("\n[bold yellow]检测到的弱化修饰词:[/bold yellow]")
            for mod in result["weak_modifiers"]["modifiers"]:
                console.print(f"  • \"{mod['modifier']}\" (出现 {mod['count']} 次)")

        if result["sentence_variation"]["starting_patterns"]:
            console.print("\n[bold blue]句子开头模式:[/bold blue]")
            for pattern in result["sentence_variation"]["starting_patterns"]:
                console.print(f"  • \"{pattern['pattern']}\" (出现 {pattern['count']} 次)")


@cli.command()
@click.argument("content1")
@click.argument("content2")
@click.option("--json", "output_json", is_flag=True, help="以JSON格式输出")
def compare(content1: str, content2: str, output_json: bool):
    """⚖️ 比较两段内容质量

    同时分析两段内容并对比它们的质量差异。

    示例:
        taste-guard compare "Text A..." "Text B..."
    """
    analyzer = ContentAnalyzer()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        progress.add_task(description="🔍 分析内容 A...", total=None)
        result1 = analyzer.analyze(content1)
        progress.add_task(description="🔍 分析内容 B...", total=None)
        result2 = analyzer.analyze(content2)

    if output_json:
        console.print(json.dumps({"content_a": result1, "content_b": result2}, ensure_ascii=False, indent=2))
        return

    # Comparison table
    table = Table(title="⚖️ 内容质量对比", box=box.ROUNDED)
    table.add_column("指标", style="cyan")
    table.add_column("内容 A", style="white")
    table.add_column("内容 B", style="white")
    table.add_column("胜出", style="green")

    score1 = result1["overall_score"]
    score2 = result2["overall_score"]
    winner = "A" if score1 > score2 else "B" if score2 > score1 else "平局"

    table.add_row(
        "整体评分",
        f"{score1:.1f}",
        f"{score2:.1f}",
        f"[bold green]{winner}[/bold green]",
    )

    table.add_row(
        "词汇多样性",
        f"{result1['viversity_metrics']['diversity_ratio']:.2f}",
        f"{result2['viversity_metrics']['diversity_ratio']:.2f}",
        "A" if result1['viversity_metrics']['diversity_ratio'] > result2['viversity_metrics']['diversity_ratio'] else "B",
    )

    table.add_row(
        "互动性",
        f"{result1['engagement_score']['score']:.1f}",
        f"{result2['engagement_score']['score']:.1f}",
        "A" if result1['engagement_score']['score'] > result2['engagement_score']['score'] else "B",
    )

    table.add_row(
        "通用短语",
        f"{result1['generic_phrases']['count']} 个",
        f"{result2['generic_phrases']['count']} 个",
        "A" if result1['generic_phrases']['count'] < result2['generic_phrases']['count'] else "B",
    )

    console.print(table)


@cli.command()
@click.argument("content", required=False)
@click.option("--file", "-f", type=click.Path(exists=True), help="从文件读取内容")
def optimize(content: Optional[str], file: Optional[str]):
    """✨ 获取优化建议

    分析内容并提供具体的优化建议，帮助提升内容质量。

    示例:
        taste-guard optimize "Your text here..."
        taste-guard optimize -f draft.txt
    """
    if file:
        try:
            content = Path(file).read_text(encoding="utf-8")
        except Exception as e:
            console.print(f"[red]读取文件失败: {e}[/red]")
            sys.exit(1)
    elif not content:
        if not sys.stdin.isatty():
            content = sys.stdin.read()
        else:
            console.print("[red]错误: 请提供文本内容或使用 --file 选项[/red]")
            sys.exit(1)

    analyzer = ContentAnalyzer()
    result = analyzer.analyze(content)

    console.print(Panel(
        f"[bold]整体评分: {result['overall_score']}/100[/bold]",
        title="✨ 优化建议",
        border_style=get_quality_color(result["overall_score"]),
    ))

    if not result["suggestions"]:
        console.print("\n[green]🎉 内容质量优秀，暂无优化建议！[/green]")
        return

    for suggestion in result["suggestions"]:
        severity_emoji = {"high": "🔴", "medium": "🟡", "low": "🔵", "info": "🟢"}
        emoji = severity_emoji.get(suggestion["severity"], "⚪")

        console.print(f"\n{emoji} [bold]{suggestion['message']}[/bold]")
        console.print(f"   [green]💡 建议: {suggestion['suggestion']}[/green]")


if __name__ == "__main__":
    cli()
