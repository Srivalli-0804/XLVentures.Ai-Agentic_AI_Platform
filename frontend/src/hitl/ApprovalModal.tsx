import React from "react";

interface ApprovalItem {
  id: string;
  company_name: string;
  contact_name: string;
  recommendation: string;
}

interface Props {
  item: ApprovalItem | null;
  isOpen: boolean;
  onApprove: (id: string) => void;
  onReject: (id: string) => void;
  onClose: () => void;
}

const ApprovalModal: React.FC<Props> = ({
  item,
  isOpen,
  onApprove,
  onReject,
  onClose
}) => {
  if (!isOpen || !item) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div className="bg-white rounded-lg w-[600px] p-6 shadow-xl">
        <h2 className="text-xl font-bold mb-4">
          Recommendation Approval
        </h2>

        <div className="space-y-3">
          <div>
            <span className="font-semibold">
              Company:
            </span>{" "}
            {item.company_name}
          </div>

          <div>
            <span className="font-semibold">
              Contact:
            </span>{" "}
            {item.contact_name}
          </div>

          <div>
            <span className="font-semibold">
              Recommendation:
            </span>
          </div>

          <div className="bg-gray-100 rounded p-3">
            {item.recommendation}
          </div>
        </div>

        <div className="flex justify-end gap-3 mt-6">
          <button
            onClick={() => onReject(item.id)}
            className="px-4 py-2 bg-red-500 text-white rounded"
          >
            Reject
          </button>

          <button
            onClick={() => onApprove(item.id)}
            className="px-4 py-2 bg-green-600 text-white rounded"
          >
            Approve
          </button>

          <button
            onClick={onClose}
            className="px-4 py-2 bg-gray-500 text-white rounded"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

export default ApprovalModal;