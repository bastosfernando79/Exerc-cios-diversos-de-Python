function maxDifference(x, y) {
    const xi = Math.abs(x[0] - y[0]);
    const yi = Math.abs(x[1] - y[1]);

    if (xi >= yi) {
        return xi;
    } else {
        return yi;
    }
}

class Solution {
    minTimeToVisitAllPoints(points) {
        let count = 0;

        for (let i = 1; i < points.length; i++) {
            const distance = maxDifference(points[i - 1], points[i]);
            count += distance;
        }

        return count;
    }
}

const solution = new Solution();
const points = [[1, 1], [3, 4], [-1, 0]];
const result = solution.minTimeToVisitAllPoints(points);
console.log(result);
