#!/usr/bin/env python3
"""
IBM Bob Academic Submission Verifier
Scans workspace files, checks for academic attribution watermarks,
validates the prompt history, audit trail, and Git commit log.
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime

def check_git_status():
    status = {"is_git_repo": False, "commit_count": 0, "commits": []}
    try:
        res = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
        if res.returncode == 0:
            status["is_git_repo"] = True
            log_res = subprocess.run(["git", "log", "--oneline", "-n", "20"], capture_output=True, text=True)
            if log_res.returncode == 0 and log_res.stdout.strip():
                lines = log_res.stdout.strip().split("\n")
                status["commit_count"] = len(lines)
                status["commits"] = lines[:10]
    except Exception as e:
        status["error"] = str(e)
    return status

def load_student_info(root_dir):
    info_path = os.path.join(root_dir, "STUDENT_INFO.json")
    if os.path.exists(info_path):
        try:
            with open(info_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def scan_files_for_watermarks(root_dir):
    ignored_dirs = {".git", ".bob", "docs", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}
    target_extensions = {".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".c", ".cpp", ".h", ".go", ".rs", ".html", ".sh", ".sql", ".css"}
    
    results = {
        "total_source_files": 0,
        "watermarked_files": [],
        "missing_watermark_files": []
    }
    
    watermark_pattern = re.compile(r"\[IBM Bob Academic Attribution\]", re.IGNORECASE)
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in ignored_dirs and not d.startswith(".")]
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in target_extensions:
                rel_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
                results["total_source_files"] += 1
                try:
                    with open(os.path.join(dirpath, filename), "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read(2048) # Read first 2KB
                        if watermark_pattern.search(content):
                            results["watermarked_files"].append(rel_path)
                        else:
                            results["missing_watermark_files"].append(rel_path)
                except Exception:
                    results["missing_watermark_files"].append(rel_path)
                    
    return results

def check_prompt_history(root_dir):
    prompt_path = os.path.join(root_dir, "PROMPT_HISTORY.md")
    if not os.path.exists(prompt_path):
        return {"exists": False, "prompt_count": 0}
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            content = f.read()
        entries = re.findall(r"###\s+\[\d{4}-\d{2}-\d{2}.*?\]\s+Prompt\s+#\d+", content, re.IGNORECASE)
        return {
            "exists": True,
            "prompt_count": len(entries),
            "size_bytes": len(content)
        }
    except Exception:
        return {"exists": True, "prompt_count": 0, "size_bytes": 0}

def check_audit_trail(root_dir):
    trail_path = os.path.join(root_dir, "AI_AUDIT_TRAIL.md")
    if not os.path.exists(trail_path):
        return {"exists": False, "entry_count": 0}
    try:
        with open(trail_path, "r", encoding="utf-8") as f:
            content = f.read()
        entries = re.findall(r"###\s+\[\d{4}-\d{2}-\d{2}", content)
        return {
            "exists": True,
            "entry_count": len(entries),
            "size_bytes": len(content)
        }
    except Exception:
        return {"exists": True, "entry_count": 0, "size_bytes": 0}

def main():
    root = os.getcwd()
    student_info = load_student_info(root)
    git_status = check_git_status()
    file_scan = scan_files_for_watermarks(root)
    prompt_history = check_prompt_history(root)
    audit_trail = check_audit_trail(root)
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "student_info": student_info,
        "git_status": git_status,
        "source_code_scan": file_scan,
        "prompt_history": prompt_history,
        "audit_trail": audit_trail
    }
    
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
