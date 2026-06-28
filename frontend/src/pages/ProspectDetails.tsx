import React from "react";

const ProspectDetails = () => {
  const prospect = {
    company_name: "OpenAI",
    industry: "Artificial Intelligence",
    score: 92,
    status: "Qualified",
    website: "https://openai.com"
  };

  return (
    <div className="p-6">
      <div className="bg-white shadow rounded-lg p-6">
        <h1 className="text-3xl font-bold">
          {prospect.company_name}
        </h1>

        <div className="mt-4 space-y-2">
          <p>
            <strong>Industry:</strong>{" "}
            {prospect.industry}
          </p>

          <p>
            <strong>Score:</strong>{" "}
            {prospect.score}
          </p>

          <p>
            <strong>Status:</strong>{" "}
            {prospect.status}
          </p>

          <p>
            <strong>Website:</strong>{" "}
            <a
              href={prospect.website}
              className="text-blue-600"
            >
              {prospect.website}
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default ProspectDetails;