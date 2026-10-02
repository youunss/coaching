#!/usr/bin/env python3
"""
Balanced Scorecard (BSC) KPI Analytics Tracker
Mobile Fitness Coaching App Operations Analysis
Author: Younss Yahya
"""

import json
import os
import sys

def load_kpi_data(filepath=None):
    if filepath is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, "kpi_data.json")
    
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def analyze_kpis(data):
    results = {}
    for kpi in data.get("kpis", []):
        name = kpi["name"]
        acronym = kpi["acronym"]
        unit = kpi["unit"]
        baseline = kpi["baseline"]
        target = kpi["target"]
        direction = kpi["direction"]
        monthly = kpi["monthly_data"]
        
        values = [m["value"] for m in monthly]
        progress_values = [m["progress_pct"] for m in monthly]
        
        avg_val = sum(values) / len(values)
        min_val = min(values)
        max_val = max(values)
        latest_val = values[-1]
        latest_prog = progress_values[-1]
        peak_prog = max(progress_values)
        
        # Calculate overall delta
        overall_change = latest_val - baseline
        
        results[acronym] = {
            "name": name,
            "unit": unit,
            "baseline": baseline,
            "target": target,
            "average": round(avg_val, 2),
            "min": min_val,
            "max": max_val,
            "latest": latest_val,
            "latest_progress": round(latest_prog, 2),
            "peak_progress": round(peak_prog, 2),
            "overall_change": round(overall_change, 2),
            "months_tracked": len(monthly)
        }
    return results

def print_dashboard():
    data = load_kpi_data()
    summary = analyze_kpis(data)
    
    print("=" * 80)
    print(f"  BALANCED SCORECARD ANALYTICS — {data['project'].upper()}")
    print(f"  Analyst: {data['author']} | Period: {data['timeframe']['start']} to {data['timeframe']['end']}")
    print("=" * 80)
    print(f"{'KPI':<30} | {'Baseline':<10} | {'Target':<10} | {'Latest':<10} | {'Progress':<10} | {'Status'}")
    print("-" * 80)
    
    for acronym, s in summary.items():
        unit = s['unit']
        base_str = f"{s['baseline']} {unit}"
        tgt_str = f"{s['target']} {unit}"
        latest_str = f"{s['latest']} {unit}"
        prog_str = f"{s['latest_progress']}%"
        status = "TARGET REACHED" if s['latest_progress'] >= 90 else "ON TRACK" if s['latest_progress'] >= 50 else "ATTENTION REQ."
        
        print(f"{s['name']:<30} | {base_str:<10} | {tgt_str:<10} | {latest_str:<10} | {prog_str:<10} | {status}")
    print("=" * 80)
    
    print("\nMONTHLY BREAKDOWN:")
    for kpi in data["kpis"]:
        print(f"\n--- {kpi['name']} ({kpi['acronym']}) [{kpi['unit']}] ---")
        print(f"{'Month':<15} | {'Value':<12} | {'Progress %':<12}")
        print("-" * 45)
        for m in kpi["monthly_data"]:
            print(f"{m['month']:<15} | {m['value']:<12} | {m['progress_pct']:>8.2f}%")

if __name__ == "__main__":
    print_dashboard()
