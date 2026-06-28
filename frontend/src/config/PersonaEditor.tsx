import React, { useState } from "react";

interface Persona {
  id: string;
  persona_name: string;
  title: string;
  department: string;
}

interface Props {
  personas: Persona[];
  onSave: (
    personas: Persona[]
  ) => void;
}

const PersonaEditor: React.FC<Props> = ({
  personas,
  onSave
}) => {
  const [data, setData] =
    useState(personas);

  const updateField = (
    index: number,
    field: keyof Persona,
    value: string
  ) => {
    const copy = [...data];

    copy[index] = {
      ...copy[index],
      [field]: value
    };

    setData(copy);
  };

  return (
    <div className="bg-white rounded-lg shadow p-5">
      <h2 className="text-xl font-bold mb-4">
        Personas
      </h2>

      {data.map((persona, index) => (
        <div
          key={persona.id}
          className="border rounded p-3 mb-3"
        >
          <input
            className="w-full border p-2 mb-2"
            value={persona.persona_name}
            onChange={(e) =>
              updateField(
                index,
                "persona_name",
                e.target.value
              )
            }
          />

          <input
            className="w-full border p-2 mb-2"
            value={persona.title}
            onChange={(e) =>
              updateField(
                index,
                "title",
                e.target.value
              )
            }
          />

          <input
            className="w-full border p-2"
            value={persona.department}
            onChange={(e) =>
              updateField(
                index,
                "department",
                e.target.value
              )
            }
          />
        </div>
      ))}

      <button
        onClick={() => onSave(data)}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Save Personas
      </button>
    </div>
  );
};

export default PersonaEditor;