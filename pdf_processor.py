#!/usr/bin/env python3
"""
PDF Processing Utilities for Advanced Constructor Team
"""

import os
import sys
import argparse
import logging
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import convert_pdf_to_markdown, batch_convert_pdfs_to_markdown, extract_pdf_metadata, organize_knowledge_base

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='PDF Processing Utilities')
    parser.add_argument('command', choices=['convert', 'batch', 'metadata', 'organize'], 
                       help='Command to execute')
    parser.add_argument('--input', '-i', required=True, help='Input PDF file or directory')
    parser.add_argument('--output', '-o', help='Output file or directory')
    
    args = parser.parse_args()
    
    try:
        if args.command == 'convert':
            if not args.input.endswith('.pdf'):
                print("Error: Input must be a PDF file for convert command")
                return 1
            result = convert_pdf_to_markdown(args.input, args.output)
            print(result)
            
        elif args.command == 'batch':
            if not os.path.isdir(args.input):
                print("Error: Input must be a directory for batch command")
                return 1
            result = batch_convert_pdfs_to_markdown(args.input, args.output)
            print(result)
            
        elif args.command == 'metadata':
            if not args.input.endswith('.pdf'):
                print("Error: Input must be a PDF file for metadata command")
                return 1
            result = extract_pdf_metadata(args.input)
            print(result)
            
        elif args.command == 'organize':
            base_path = args.input if os.path.isdir(args.input) else "library_KB"
            result = organize_knowledge_base(base_path)
            print(result)
            
        return 0
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())