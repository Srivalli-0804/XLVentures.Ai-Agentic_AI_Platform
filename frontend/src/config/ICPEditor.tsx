import React, { useState } from "react";

interface ICPConfig {
  industries: string[];
  company_sizes: string[];
  technologies: string[];
  regions: string[];
}

interface Props {
  initialConfig: ICPConfig;
  onSave: (config: ICPConfig) => void;
}

const ICPEditor: React.FC<Props> = ({
  initialConfig,
  onSave
}) => {
  const [config, setConfig] =
    useState(initialConfig);

  const updateField = (
    field: keyof ICPConfig,
    value: string
  ) => {
    setConfig({
      ...config,
      [field]: value
        .split(",")
        .map((item) => item.trim())
    });
  };

  return (
    <div className="bg-white rounded-lg shadow p-5">
      <h2 className="text-xl font-bold mb-4">
        ICP Configuration
      </h2>

      <div className="space-y-4">
        <input
          className="w-full border p-2 rounded"
          placeholder="Industries"
          value={config.industries.join(", ")}
          onChange={(e) =>
            updateField(
              "industries",
              e.target.value
            )
          }
        />

        <input
          className="w-full border p-2 rounded"
          placeholder="Company Sizes"
          value={config.company_sizes.join(", ")}
          onChange={(e) =>
            updateField(
              "company_sizes",
              e.target.value
            )
          }
        />

        <input
          className="w-full border p-2 rounded"
          placeholder="Technologies"
          value={config.technologies.join(", ")}
          onChange={(e) =>
            updateField(
              "technologies",
              e.target.value
            )
          }
        />

        <input
          className="w-full border p-2 rounded"
          placeholder="Regions"
          value={config.regions.join(", ")}
          onChange={(e) =>
            updateField(
              "regions",
              e.target.value
            )
          }
        />

        <button
          onClick={() => onSave(config)}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Save ICP
        </button>
      </div>
    </div>
  );
};

export default ICPEditor;