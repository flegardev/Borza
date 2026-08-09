import { expect, test } from "@playwright/test";
import pathPayload from "../../content/academy/paths.json";

test("catalogue separates active paths from the non-interactive roadmap", async ({
  page,
}, testInfo) => {
  const browserErrors: string[] = [];
  page.on("console", (message) => {
    if (message.type() === "error") browserErrors.push(message.text());
  });
  page.on("pageerror", (error) => browserErrors.push(error.message));

  await page.addInitScript(() => {
    window.localStorage.setItem("borza-academy-language", "en");
    window.localStorage.setItem("borza-academy-theme", "light");
  });
  await page.route("**/api/v1/**", async (route) => {
    if (new URL(route.request().url()).pathname.endsWith("/learning-paths")) {
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify(
          pathPayload.paths.map((path) => ({
            ...path,
            lesson_count: path.status === "active" ? 8 : 0,
            module_count: path.status === "active" ? 6 : 0,
          })),
        ),
      });
      return;
    }
    await route.fulfill({ status: 204 });
  });

  const response = await page.goto("/learn", { waitUntil: "domcontentloaded" });
  expect(response?.status()).toBeLessThan(400);

  const active = page.getByRole("region", { name: "Active learning paths" });
  await expect(active.getByRole("link", { name: /Open path/ })).toHaveCount(4);

  const roadmap = page.getByRole("region", { name: "Roadmap" });
  await expect(roadmap.getByText("Planned", { exact: true })).toHaveCount(8);
  await expect(roadmap.getByRole("link")).toHaveCount(0);
  await expect(roadmap.getByText("Economics for Markets")).toBeVisible();
  await expect(page.getByText("12", { exact: true })).toBeVisible();
  expect(browserErrors).toEqual([]);

  await page.screenshot({
    path: testInfo.outputPath("catalogue.png"),
    fullPage: true,
  });
});
