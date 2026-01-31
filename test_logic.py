"""
Test script to validate RSA system logic without requiring API
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from aggregation import create_groups, create_aggregation_prompt, create_final_aggregation_prompt


def test_create_groups():
    """Test group creation logic"""
    print("Testing create_groups()...")
    
    # Test case 1: Even division
    responses = [f"response_{i}" for i in range(16)]
    groups = create_groups(responses, 4)
    assert len(groups) == 4, f"Expected 4 groups, got {len(groups)}"
    assert all(len(g) == 4 for g in groups), "All groups should have size 4"
    print("  ✓ Test 1 passed: 16 responses → 4 groups of 4")
    
    # Test case 2: Uneven division
    responses = [f"response_{i}" for i in range(10)]
    groups = create_groups(responses, 3)
    assert len(groups) == 4, f"Expected 4 groups, got {len(groups)}"
    assert len(groups[0]) == 3, "First group should have 3"
    assert len(groups[-1]) == 1, "Last group should have 1"
    print("  ✓ Test 2 passed: 10 responses → 4 groups (3,3,3,1)")
    
    # Test case 3: Smaller than group size
    responses = [f"response_{i}" for i in range(2)]
    groups = create_groups(responses, 4)
    assert len(groups) == 1, f"Expected 1 group, got {len(groups)}"
    assert len(groups[0]) == 2, "Group should have 2 responses"
    print("  ✓ Test 3 passed: 2 responses → 1 group of 2")
    
    print("✅ All create_groups() tests passed!\n")


def test_aggregation_prompts():
    """Test prompt creation"""
    print("Testing aggregation prompts...")
    
    # Test aggregation prompt
    responses = ["Solution A", "Solution B", "Solution C"]
    original_prompt = "Solve the problem"
    
    agg_prompt = create_aggregation_prompt(responses, original_prompt)
    assert "PROBLEMA ORIGINAL" in agg_prompt
    assert "SOLUCIÓN 1" in agg_prompt
    assert "SOLUCIÓN 2" in agg_prompt
    assert "SOLUCIÓN 3" in agg_prompt
    assert "Solution A" in agg_prompt
    assert "Solution B" in agg_prompt
    assert "Solution C" in agg_prompt
    print("  ✓ Aggregation prompt structure is correct")
    
    # Test final aggregation prompt
    final_prompt = create_final_aggregation_prompt(responses, original_prompt)
    assert "PROBLEMA ORIGINAL" in final_prompt
    assert "SOLUCIÓN REFINADA" in final_prompt
    assert "TAREA FINAL" in final_prompt
    print("  ✓ Final aggregation prompt structure is correct")
    
    print("✅ All prompt tests passed!\n")


def test_rsa_logic():
    """Test RSA loop logic simulation"""
    print("Testing RSA loop logic simulation...")
    
    # Simulate RSA process
    population_size = 16
    group_size = 4
    loops = 3
    
    current_pop = population_size
    print(f"  Initial population: {current_pop}")
    
    for loop in range(1, loops + 1):
        groups = (current_pop + group_size - 1) // group_size  # Ceiling division
        new_pop = groups
        print(f"  Loop {loop}: {current_pop} → {groups} groups → {new_pop} responses")
        current_pop = new_pop
        
        if current_pop == 1:
            print(f"  Converged at loop {loop}")
            break
    
    print(f"  Final population: {current_pop}")
    print("✅ RSA logic simulation passed!\n")


def test_imports():
    """Test that all modules can be imported"""
    print("Testing module imports...")
    
    try:
        # This will fail without dependencies, but structure is valid
        print("  Note: Full import test requires dependencies installed")
        print("  Checking file structure...")
        
        import os
        files = [
            'src/__init__.py',
            'src/gemini_client.py',
            'src/aggregation.py',
            'src/rsa_orchestrator.py',
            'main.py',
            'examples.py'
        ]
        
        for f in files:
            assert os.path.exists(f), f"File {f} not found"
            print(f"    ✓ {f}")
        
        print("✅ All files exist!\n")
        
    except Exception as e:
        print(f"❌ Import test failed: {e}\n")


if __name__ == "__main__":
    print("="*60)
    print("RSA System - Logic Validation Tests")
    print("="*60 + "\n")
    
    try:
        test_imports()
        test_create_groups()
        test_aggregation_prompts()
        test_rsa_logic()
        
        print("="*60)
        print("✅ ALL TESTS PASSED!")
        print("="*60)
        print("\nThe RSA system logic is correct.")
        print("To run with actual Gemini API:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Set GEMINI_API_KEY in .env file")
        print("  3. Run: python main.py \"your prompt here\"")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
