#!/usr/bin/env python3
"""
Unit tests for BSC KPI Analytics Tracker
"""

import unittest
from kpi_tracker import load_kpi_data, analyze_kpis

class TestKPITracker(unittest.TestCase):
    def setUp(self):
        self.data = load_kpi_data()

    def test_data_integrity(self):
        self.assertEqual(self.data["project"], "Mobile Fitness Coaching App")
        self.assertEqual(len(self.data["kpis"]), 3)

    def test_analysis_calculation(self):
        summary = analyze_kpis(self.data)
        self.assertIn("ART", summary)
        self.assertIn("FCR", summary)
        self.assertIn("CSAT", summary)

        art = summary["ART"]
        self.assertEqual(art["baseline"], 18.0)
        self.assertEqual(art["target"], 2.0)
        self.assertEqual(art["latest"], 2.5)
        self.assertGreater(art["latest_progress"], 95.0)

        csat = summary["CSAT"]
        self.assertEqual(csat["baseline"], 60.0)
        self.assertEqual(csat["target"], 97.0)
        self.assertEqual(csat["latest"], 84.0)

if __name__ == "__main__":
    unittest.main()
