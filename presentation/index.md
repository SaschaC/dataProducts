---
title: Stress Position in German Words
framework: revealjs
revealjs: {theme: solarized, transition: convex}
mode: selfcontained
url: {lib: ../libraries}

---

# Stress Position in German words
A Shiny app
<p><small>by Sascha C.</small></p>

---

## What is word stress?

The **stressed syllable** within a word is the most prominent syllable  . This prominence can be expressed via:

* Loudness
* Length
* Pitch

For example, in English '<span style="color:red">Ba</span>by', the syllable -ba is the most prominent syllable.

---

## German word stress

In German (and English), stress position varies between words. Examples: <span class="stress">Bei</span>spiel, Zer<span class ="stress">brech</span>lichkeit, unter<span class ="stress">hal</span>ten, kontrol<span class="stress">lie</span>ren

Some **regularities** exist, e.g., most (all?) unprefixed words that are not loan words are stressed on the first syllable.

However, the distribution of German word stress is not clear. E.g., how often does stress occur on the second syllable of a word?

--- 

## App data base

The data base consists of 44,378 words selected from <a href="https://catalog.ldc.upenn.edu/ldc96l14">CELEX lexical database for German</a>. 

The selection criteria were:
* Word type = Adjective, Noun, or Verb
* Minimally 2 syllables, maximally 5 syllables

These words were extracted along with information on: 
* Word frequency
* Syllable number
* <span style="border-bottom: dotted 1px blue" title="where position n signifies stress on the nth syllable">Stress position</span>
* Word type (Adjective, Noun, Verb)

An excerpt of the app data base can be found <a href="">here</a>.

---

## App functionality

Research question: How is stress position in German distributed accross words?

Functions:
<ul>
  <li>Plot word <span style="border-bottom: dotted 1px blue" title="where position n signifies stress on the nth syllable">stress position</span> as a function of <em>word type</em> and <em>syllable number</em>
  <ul>
    <li>Word type: Adjective, Noun, Verb</li>
    <li>Syllable number: from 2 to 5 syllables</li>
  </ul>
  <li>Control for <em>word frequency</em></li>
  <ul>
    <li>For example, restrict analysis to words with a minimal frequency of 1000.</li>
  </ul>
</ul>

