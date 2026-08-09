import { describe, expect, it } from "vitest";
import type { LearningPathSummary } from "@/lib/academy-types";
import { partitionCataloguePaths } from "./catalog-paths";

const text = { de: "Titel", sl: "Naslov", en: "Title" };

function path(
  id: string,
  status: LearningPathSummary["status"],
): LearningPathSummary {
  return {
    id,
    title: text,
    summary: text,
    difficulty: "beginner",
    estimatedMinutes: status === "active" ? 240 : 0,
    lessonCount: status === "active" ? 8 : 0,
    status,
    previewTopics: { de: [], sl: [], en: [] },
  };
}

describe("partitionCataloguePaths", () => {
  it("keeps roadmap-only paths out of the active catalogue", () => {
    const result = partitionCataloguePaths([
      path("path-finance-foundations", "active"),
      path("path-economics-for-markets", "coming_next"),
      path("path-risk-management", "active"),
    ]);

    expect(result.activePaths.map((item) => item.id)).toEqual([
      "path-risk-management",
      "path-finance-foundations",
    ]);
    expect(result.roadmapPaths.map((item) => item.id)).toEqual([
      "path-economics-for-markets",
    ]);
  });
});
