#!/bin/bash
# Task 1 Completion Test Script
# This script verifies that all Task 1 requirements are met

echo "🧪 Testing Hidden Hill Backend (Task 1)"
echo "======================================"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

passed=0
failed=0

# Test 1: Health endpoint
echo -n "✓ Testing health endpoint... "
response=$(curl -s http://localhost:8000/health/ | grep -o '"status":"ok"')
if [ ! -z "$response" ]; then
    echo -e "${GREEN}PASS${NC}"
    ((passed++))
else
    echo -e "${RED}FAIL${NC}"
    ((failed++))
fi

# Test 2: Root endpoint
echo -n "✓ Testing root endpoint... "
response=$(curl -s http://localhost:8000/ | grep -o "Hidden Hill API is running")
if [ ! -z "$response" ]; then
    echo -e "${GREEN}PASS${NC}"
    ((passed++))
else
    echo -e "${RED}FAIL${NC}"
    ((failed++))
fi

# Test 3: Generate video endpoint
echo -n "✓ Testing generate video endpoint... "
response=$(curl -s -X POST http://localhost:8000/api/videos/generate \
  -H "Content-Type: application/json" \
  -d '{"pubmed_id": "PMC10979640"}' | grep -o '"job_id"')
if [ ! -z "$response" ]; then
    echo -e "${GREEN}PASS${NC}"
    ((passed++))
    # Extract job_id for next test
    job_id=$(curl -s -X POST http://localhost:8000/api/videos/generate \
      -H "Content-Type: application/json" \
      -d '{"pubmed_id": "PMC99999999"}' | grep -o '"job_id":"[^"]*' | cut -d'"' -f4)
else
    echo -e "${RED}FAIL${NC}"
    ((failed++))
fi

# Test 4: Get job status endpoint
echo -n "✓ Testing get status endpoint... "
if [ ! -z "$job_id" ]; then
    response=$(curl -s http://localhost:8000/api/videos/$job_id | grep -o '"status":"pending"')
    if [ ! -z "$response" ]; then
        echo -e "${GREEN}PASS${NC}"
        ((passed++))
    else
        echo -e "${RED}FAIL${NC}"
        ((failed++))
    fi
fi

# Test 5: Download endpoint (should fail - video not complete)
echo -n "✓ Testing download endpoint error handling... "
status=$(curl -s -w "%{http_code}" -o /dev/null http://localhost:8000/api/videos/$job_id/download)
if [ "$status" = "409" ]; then
    echo -e "${GREEN}PASS${NC} (HTTP 409 as expected)"
    ((passed++))
else
    echo -e "${RED}FAIL${NC} (Expected 409, got $status)"
    ((failed++))
fi

# Test 6: 404 for invalid job ID
echo -n "✓ Testing 404 error handling... "
status=$(curl -s -w "%{http_code}" -o /dev/null http://localhost:8000/api/videos/invalid-id)
if [ "$status" = "404" ]; then
    echo -e "${GREEN}PASS${NC}"
    ((passed++))
else
    echo -e "${RED}FAIL${NC} (Expected 404, got $status)"
    ((failed++))
fi

# Test 7: Validation error for empty pubmed_id
echo -n "✓ Testing validation... "
status=$(curl -s -w "%{http_code}" -o /dev/null -X POST http://localhost:8000/api/videos/generate \
  -H "Content-Type: application/json" \
  -d '{"pubmed_id": ""}')
if [ "$status" = "422" ]; then
    echo -e "${GREEN}PASS${NC}"
    ((passed++))
else
    echo -e "${RED}FAIL${NC} (Expected 422, got $status)"
    ((failed++))
fi

# Test 8: Email validation
echo -n "✓ Testing email validation... "
status=$(curl -s -w "%{http_code}" -o /dev/null -X POST http://localhost:8000/api/videos/generate \
  -H "Content-Type: application/json" \
  -d '{"pubmed_id": "PMC123", "user_email": "invalid"}')
if [ "$status" = "422" ]; then
    echo -e "${GREEN}PASS${NC}"
    ((passed++))
else
    echo -e "${RED}FAIL${NC} (Expected 422, got $status)"
    ((failed++))
fi

# Test 9: Swagger docs
echo -n "✓ Testing Swagger docs... "
status=$(curl -s -w "%{http_code}" -o /dev/null http://localhost:8000/docs)
if [ "$status" = "200" ]; then
    echo -e "${GREEN}PASS${NC}"
    ((passed++))
else
    echo -e "${RED}FAIL${NC} (Expected 200, got $status)"
    ((failed++))
fi

echo ""
echo "======================================"
echo -e "Results: ${GREEN}${passed} passed${NC}, ${RED}${failed} failed${NC}"
echo "======================================"

if [ $failed -eq 0 ]; then
    echo -e "${GREEN}✅ All Task 1 tests passed!${NC}"
    exit 0
else
    echo -e "${RED}❌ Some tests failed${NC}"
    exit 1
fi
