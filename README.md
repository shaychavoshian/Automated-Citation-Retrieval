# Automated-Citation-Retrieval


<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## 📚 Project Overview
Hello 👋
Welcome to the Automated Citation Retrieval project! 🌐✨
This project simplifies the process of gathering bibliographic data for literature reviews by automating citation extraction from multiple databases.

## 📖 Project Description
For our literature review, we used Covidence to manage and screen relevant articles. Bibliographic data was manually downloaded from PubMed, Scopus, IEEE Xplore, and Web of Science using their export functionalities. However, due to the lack of an efficient bulk export feature in Google Scholar, we developed a Python script to streamline the citation retrieval process and automate the extraction of publication metadata.

### 🎯 Key Features
- **Automated Metadata Extraction:** The script interfaces with Google Scholar to collect bibliographic details such as titles, authors, publication year, journal names, and abstracts.
- **RIS Export Support:** Citations are exported into the RIS format for easy reference management.
- **Efficiency Considerations:** The script includes a delay between each request to prevent overwhelming servers and avoid triggering anti-bot mechanisms.
- **Multi-Database Compatibility:** Supports data extraction from multiple academic databases for comprehensive literature reviews.

## 🛠️ How It Works
1. **Input Search Query:** Provide a search query directly in the script.
2. **Automated Retrieval:** The script searches Google Scholar and other databases for relevant publications.
3. **Data Export:** Export results in RIS format for easy import into citation managers like Mendeley or Zotero.
4. **Rate Limiting:** A built-in delay prevents excessive server requests.

## 🚀 Why Share This Project?
Sharing this tool encourages collaboration and helps streamline the research process for others facing similar challenges with citation retrieval. Automating citation collection saves significant time while ensuring a comprehensive literature review.

## 🚫 Why Not Share Everything?
Some portions of the tool may not be shared due to:
- **Privacy Considerations:** User-specific credentials or API keys are excluded.
- **Data Access Restrictions:** Google Scholar terms of use may limit automated scraping practices.
- **Intellectual Property:** Parts of the code directly linked to proprietary datasets may remain private.

## ✅ Checklist for Citation Retrieval Project
- [ ] Develop a Python script for automated citation extraction.
- [ ] Implement delay mechanisms for responsible scraping.
- [ ] Ensure compatibility with RIS export format.
- [ ] Validate citation accuracy across databases.
- [ ] Share the script with research collaborators.

---

## 👥 The Team
**Lead Developer:** Shaghayegh Chavoshian
**Project Lead:** Ali Barzegar
**Supervisor:** Principal Investigator


📫 **Contact:** [shay.chavoshian@mail.utoronto.ca](mailto:shay.chavoshian@mail.utoronto.ca)

---

## 🏆 License
This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.

