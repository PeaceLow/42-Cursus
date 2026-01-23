import subprocess
import random
import sys
import statistics

# ANSI Color Codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def run_push_swap(numbers, strategy=None):
    args = [str(n) for n in numbers]
    cmd = ['./push_swap']
    if strategy:
        cmd.append(strategy)
    cmd.extend(args)
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if stderr:
             pass
        return stdout.strip().split('\n')
    except Exception as e:
        print(f"Failed to run push_swap: {e}")
        return []

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def apply_operations(numbers, operations):
    a = list(numbers)
    b = []
    
    for op in operations:
        op = op.strip()
        if not op: continue
        
        if op == "sa":
            if len(a) > 1: a[0], a[1] = a[1], a[0]
        elif op == "sb":
            if len(b) > 1: b[0], b[1] = b[1], b[0]
        elif op == "ss":
            if len(a) > 1: a[0], a[1] = a[1], a[0]
            if len(b) > 1: b[0], b[1] = b[1], b[0]
        elif op == "pa":
            if b: a.insert(0, b.pop(0))
        elif op == "pb":
            if a: b.insert(0, a.pop(0))
        elif op == "ra":
            if len(a) > 1: a.append(a.pop(0))
        elif op == "rb":
            if len(b) > 1: b.append(b.pop(0))
        elif op == "rr":
            if len(a) > 1: a.append(a.pop(0))
            if len(b) > 1: b.append(b.pop(0))
        elif op == "rra":
            if len(a) > 1: a.insert(0, a.pop())
        elif op == "rrb":
            if len(b) > 1: b.insert(0, b.pop())
        elif op == "rrr":
            if len(a) > 1: a.insert(0, a.pop())
            if len(b) > 1: b.insert(0, b.pop())
        else:
            return None, None
            
    return a, b

def test_size(size, iterations=20, max_ops=None, test_name="", strategy=None):
    ops_counts = []
    failed = False
    
    for _ in range(iterations):
        numbers = random.sample(range(-10000, 10000), size)
        ops = run_push_swap(numbers, strategy)
        ops = [op for op in ops if op]
        
        final_a, final_b = apply_operations(numbers, ops)
        
        if final_a is None:
            print(f"{Colors.RED}❌ Failed on size {size}: Invalid operation{Colors.ENDC}")
            failed = True
            break
            
        if not is_sorted(final_a) or len(final_a) != size or final_b:
            print(f"{Colors.RED}❌ Failed on size {size}: Not sorted or logic error{Colors.ENDC}")
            print(f"Initial: {numbers}")
            failed = True
            break
        
        ops_count = len(ops)
        ops_counts.append(ops_count)
        
    if not failed:
        avg = statistics.mean(ops_counts)
        min_ops = min(ops_counts)
        max_ops_result = max(ops_counts)
        
        # Check if AVERAGE exceeds limit, not individual tests
        exceeded = max_ops and avg > max_ops
        
        print(f"{Colors.CYAN}{Colors.BOLD}{test_name}{Colors.ENDC}")
        print(f"  {Colors.BLUE}Taille:{Colors.ENDC} {size} éléments")
        print(f"  {Colors.BLUE}Itérations:{Colors.ENDC} {iterations}")
        print(f"  {Colors.BLUE}Min:{Colors.ENDC} {min_ops} ops  {Colors.BLUE}|{Colors.ENDC}  {Colors.BLUE}Max:{Colors.ENDC} {max_ops_result} ops  {Colors.BLUE}|{Colors.ENDC}  {Colors.BLUE}Moyenne:{Colors.ENDC} {avg:.2f} ops")
        
        if max_ops:
            margin = max_ops - avg
            percentage = (avg / max_ops) * 100
            if exceeded:
                status = f"{Colors.RED}❌ ÉCHEC{Colors.ENDC}"
            else:
                status = f"{Colors.GREEN}✅ RÉUSSI{Colors.ENDC}"
            print(f"  {Colors.BLUE}Limite:{Colors.ENDC} {max_ops} ops  {Colors.BLUE}|{Colors.ENDC}  {Colors.BLUE}Utilisation:{Colors.ENDC} {percentage:.1f}%  {Colors.BLUE}|{Colors.ENDC}  {Colors.BLUE}Marge:{Colors.ENDC} {margin:.0f} ops")
            print(f"  {Colors.BLUE}Status:{Colors.ENDC} {status}")
    print()
    
    return {
        "passed": not failed and not exceeded,
        "avg": statistics.mean(ops_counts) if ops_counts else 0,
        "min": min(ops_counts) if ops_counts else 0,
        "max": max(ops_counts) if ops_counts else 0,
        "limit": max_ops,
        "size": size
    }

def test_simple():
    """Test simple cases (3 and 5 elements)"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}║          TESTS SIMPLES                 ║{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    result_3 = test_size(3, iterations=20, max_ops=3, test_name="Test Simple - 3 éléments", strategy="--simple")
    result_5 = test_size(5, iterations=20, max_ops=12, test_name="Test Simple - 5 éléments", strategy="--simple")
    return {
        "passed": result_3["passed"] and result_5["passed"],
        "tests": [result_3, result_5]
    }

def test_medium():
    """Test medium cases (100 elements)"""
    print(f"\n{Colors.YELLOW}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}║          TESTS MOYENS                  ║{Colors.ENDC}")
    print(f"{Colors.YELLOW}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    result = test_size(100, iterations=100, max_ops=700, test_name="Test Moyen - 100 éléments", strategy="--adaptive")
    return {
        "passed": result["passed"],
        "tests": [result]
    }

def test_complex():
    """Test complex cases (500 and 1000 elements)"""
    print(f"\n{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}║          TESTS COMPLEXES               ║{Colors.ENDC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════╝{Colors.ENDC}\n")
    result_500 = test_size(500, iterations=100, max_ops=5500, test_name="Test Complexe - 500 éléments", strategy="--adaptive")
    return {
        "passed": result_500["passed"],
        "tests": [result_500]
    }

if __name__ == "__main__":
    results = {
        "Simple": test_simple(),
        "Medium": test_medium(),
        "Complex": test_complex()
    }
    
    # Display comparison table
    print(f"\n{Colors.BOLD}{Colors.HEADER}╔════════════════════════════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}║                    TABLEAU COMPARATIF                          ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}╚════════════════════════════════════════════════════════════════╝{Colors.ENDC}\n")
    
    # Table header
    print(f"{Colors.BOLD}{'Catégorie':<15} {'Taille':<10} {'Moyenne':<12} {'Limite':<12} {'Efficacité':<12} {'Status':<10}{Colors.ENDC}")
    print(f"{Colors.BLUE}{'─'*80}{Colors.ENDC}")
    
    # Gather all test results
    all_tests = []
    for category_name, category_result in results.items():
        for test in category_result["tests"]:
            efficiency = (test["avg"] / test["limit"]) * 100 if test["limit"] else 0
            status = f"{Colors.GREEN}✅ OK{Colors.ENDC}" if test["passed"] else f"{Colors.RED}❌ KO{Colors.ENDC}"
            
            # Color code efficiency
            if efficiency < 50:
                eff_color = Colors.GREEN
            elif efficiency < 75:
                eff_color = Colors.YELLOW
            else:
                eff_color = Colors.RED
            
            print(f"{Colors.CYAN}{category_name:<15}{Colors.ENDC} "
                  f"{test['size']:<10} "
                  f"{test['avg']:<12.2f} "
                  f"{test['limit']:<12} "
                  f"{eff_color}{efficiency:<11.1f}%{Colors.ENDC} "
                  f"{status}")
            all_tests.append(test)
    
    # Summary
    print(f"\n{Colors.BOLD}{Colors.HEADER}╔════════════════════════════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}║                         RÉSUMÉ FINAL                           ║{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}╚════════════════════════════════════════════════════════════════╝{Colors.ENDC}\n")
    
    for test_name, category_result in results.items():
        passed = category_result["passed"]
        status = f"{Colors.GREEN}✅ RÉUSSI{Colors.ENDC}" if passed else f"{Colors.RED}❌ ÉCHOUÉ{Colors.ENDC}"
        print(f"  {Colors.BOLD}{test_name:.<20}{Colors.ENDC} {status}")
    
    all_passed = all(r["passed"] for r in results.values())
    
    print(f"\n{Colors.BOLD}{'═'*64}{Colors.ENDC}")
    if all_passed:
        print(f"{Colors.GREEN}{Colors.BOLD}           🎉 TOUS LES TESTS SONT RÉUSSIS ! 🎉{Colors.ENDC}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}           ⚠️  CERTAINS TESTS ONT ÉCHOUÉ ⚠️{Colors.ENDC}")
    print(f"{Colors.BOLD}{'═'*64}{Colors.ENDC}\n")
    
    if not all_passed:
        sys.exit(1)