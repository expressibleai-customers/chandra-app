-- Database Migration Script-- Generated: 2025-10-19T16:35:03.399846+00:00-- Database: postgresqlCREATE TABLE user_managements (
    id SERIAL PRIMARY KEY NOT NULL,
    role TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_user_managements_created_at ON user_managements(created_at);
ALTER TABLE user_managements ADD CONSTRAINT chk_user_managements_role CHECK (role IN ('caregiver', 'care_receiver', 'care_provider', 'business'));

CREATE TABLE resource_managements (
    id SERIAL PRIMARY KEY NOT NULL,
    filtering TEXT,
    categorization TEXT,
    content_management_capabilities TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_resource_managements_created_at ON resource_managements(created_at);

CREATE TABLE community_platforms (
    id SERIAL PRIMARY KEY NOT NULL,
    community_management TEXT,
    moderation_tools TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_community_platforms_created_at ON community_platforms(created_at);

CREATE TABLE ai_assistants (
    id SERIAL PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    relevant TEXT,
    helpful_responses TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_ai_assistants_created_at ON ai_assistants(created_at);

CREATE TABLE care_provider_portals (
    id SERIAL PRIMARY KEY NOT NULL,
    caregivers TEXT,
    care_receivers TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_care_provider_portals_created_at ON care_provider_portals(created_at);

