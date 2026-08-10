import type { LearningPathSummary } from "@/lib/academy-types";

export function partitionCataloguePaths(paths: LearningPathSummary[]) {
  const activePaths = paths
    .filter((path) => path.status === "active")
    .sort((a, b) =>
      a.id === "path-risk-management"
        ? -1
        : b.id === "path-risk-management"
          ? 1
          : 0,
    );
  const roadmapPaths = paths.filter((path) => path.status === "coming_next");

  return { activePaths, roadmapPaths };
}
